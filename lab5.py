import random
import string
passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)
    

    dict = {}
    letters = random.sample(string.ascii_lowercase, 5)
    replacements_count = 0

    for letter in letters:
        replacements = set()
        while len(replacements) < 3:
            replacement_char = random.choice(string.punctuation + string.digits + string.ascii_uppercase)
            replacements.add(replacement_char)
        dict[letter] = list(replacements)
        replacements_count = replacements_count + 1


    passwords = [''.join(random.choices(string.ascii_lowercase, k=15)) for _ in range(5)]


    def replace_chars(password, dict):
        modified_password = []
        for char in password:
            if char in dict:
                modified_password.append(random.choice(dict[char]))
            else:
                modified_password.append(char)
        return ''.join(modified_password)


    modified_passwords = [replace_chars(password, dict) for password in passwords]

    print("\n".join(passwords)+ " "+"origanal passwords")
    print("\n modified passwords:")
    print("\n".join(modified_passwords))
    print(dict)
    if (replacements_count < 4):
        print("strong password")
    else:
        print("weak password")
