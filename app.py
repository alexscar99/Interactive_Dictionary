import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def get_definition(w):
    w = w.lower()
    if w in data:
        return data[w]
    # Handle proper nouns (Texas, Paris, Delhi, etc.)
    elif w.capitalize() in data:
        return data[w.capitalize()]
    # Handle abbreviations and acronyms (USA, NATO, etc.)
    elif w.upper() in data:
        return data[w.upper()]
    # Handle user typos by finding a close match
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        # Use string formatter as placeholder for the expression declared
        # after string. Return first close match from list.
        yes_or_no = input(
            'Did you mean %s instead? Enter Y if yes or N if no: ' %
            get_close_matches(w, data.keys())[0])
        if yes_or_no == 'Y' or yes_or_no == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yes_or_no == 'N' or yes_or_no == 'n':
            return 'The word does not exist. Please double check it.'
        else:
            return 'Entry was not understood.'
    else:
        return 'The word does not exist. Please double check it.'


word = input('Enter word: ')

output = get_definition(word)

# `output` will return either a list of definitions if the word exists in the
#  dictionary or a message (str) to handle user interaction. Iterate through
# if it's a list and print each definition on a new line. Conditional check to
# print a numbered list only if more than one definition exists.
if type(output) == list:
    for item in output:
        if len(output) > 1:
            definition_count = str(output.index(item) + 1)
            print(definition_count + ') ' + item)
        else:
            print(item)
else:
    print(output)
