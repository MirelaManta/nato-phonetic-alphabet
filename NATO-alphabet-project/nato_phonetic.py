
import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_phonetic_alphabet)


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        user_input_phonetic = [nato_phonetic_alphabet[letter] for letter in user_input]
    except KeyError:
        print("Sorry, there are only letters in the alphabet. Try again.")
        generate_phonetic()
    else:
        print(user_input_phonetic)


generate_phonetic()