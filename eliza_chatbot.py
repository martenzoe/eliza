# Set initial prompt and keywords
from enum import nonmember

prompt = "Is anything troubling you?"
verbs = ['avoid', 'worry', 'fear']
nouns = ["mother", "Python", "the sandman"]

while True:
    # Prompt user, in uppercase, with newline at the end
    user_input = input(prompt.upper() + '\n')

    # Quit if user typed q
    if user_input == 'q':
        print("That's all for today.")
        break

    # Set default prompt
    prompt = "Tell me more."

    # Check if user used keyword
    # Check if user used keyword
    for verb in verbs:
        if verb in user_input:
            start = user_input.find(verb)
            end = user_input.find('.')
            if end == -1:
                end = len(user_input)
            partial_response = user_input[start:end]
            prompt = f"Why do you {partial_response}?"

    for key_noun in nouns:
        if key_noun in user_input:
            prompt = f"What made you think of {key_noun}"