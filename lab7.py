def add(x,y):
    return x+y
def multiply(x,y):
    return x*y
def subtract(x, y):
    return x-y
def divide(x,y):
    return x/y
def power(x,y):
    return x**y
def mod(x,y):
    return x%y
if __name__ == "__main__":
    # Basit test örnekleri
    a, b = 10, 5
    print("Test Cases for math_utils:")
    print(f"{a} + {b} =", add(a, b))
    print(f"{a} - {b} =", subtract(a, b))
    print(f"{a} * {b} =", multiply(a, b))
    print(f"{a} / {b} =", divide(a, b))
    print(f"{a} ^ {b} =", power(a, b))
    print(f"{a} % {b} =", mod(a, b))
    # Division by zero örneği
    print(f"{a} / 0 =", divide(a, 0))




import math_utils

print(math_utils.add(5, 3))
print(math_utils.subtract(5, 3))
print(math_utils.multiply(5, 3))
print(math_utils.divide(5, 3))
print(math_utils.power(5, 3))
print(math_utils.mod(5, 3))

import math_utils


def get_input():
    try:
        operator = int(
            input("Enter operator:\n1 for add\n2 for multiply\n3 for subtract\n4 for divide\n5 for power\n6 for mod\n"))
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None, None

    return num1, operator, num2


def calculate(num1, operator, num2):

    operations = {
        1: math_utils.add,
        2: math_utils.multiply,
        3: math_utils.subtract,
        4: math_utils.divide,
        5: math_utils.power,
        6: math_utils.mod
    }

    func = operations.get(operator)
    if func is None:
        print("Invalid operator selected.")
        return None
    return func(num1, num2)


def main():
    num1, operator, num2 = get_input()
    if num1 is None:
        return

    result = calculate(num1, operator, num2)
    if result is not None:
        print("Result:", result)
    else:
        print("Calculation could not be performed.")


if __name__ == "__main__":
    main()


#string_package2/manipulate.py

import string

def reverse_string(s):

    return s[::-1]

def capitalize_words(s):

    return s.title()

def remove_punctuation(s):

    translator = str.maketrans('', '', string.punctuation)
    return s.translate(translator)
#string_package2/stats.py

def count_characters(s):

    return len(s.replace(" ", ""))

def count_words(s):

    return len(s.split())

def average_word_length(s):

    words = s.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)

from .manipulate import reverse_string, capitalize_words, remove_punctuation
from .stats import count_characters, count_words, average_word_length
# string_analyzer.py

from string_package import (
    reverse_string,
    capitalize_words,
    remove_punctuation,
    count_characters,
    count_words,
    average_word_length
)


def main():
    sentence = input("Enter a sentence: ")

    # Manipülasyon işlemleri
    reversed_sentence = reverse_string(sentence)
    capitalized_sentence = capitalize_words(sentence)
    sentence_no_punct = remove_punctuation(sentence)

    # İstatistik hesaplamaları (noktalama kaldırılmış haliyle)
    char_count = count_characters(sentence_no_punct)
    word_count = count_words(sentence_no_punct)
    avg_word_len = average_word_length(sentence_no_punct)

    # Sonuçları ekrana yazdır
    print("\n--- String Analysis Results ---")
    print("Reversed Sentence:       ", reversed_sentence)
    print("Capitalized Sentence:    ", capitalized_sentence)
    print("Without Punctuation:     ", sentence_no_punct)
    print("Character Count (no spaces):", char_count)
    print("Word Count:              ", word_count)
    print("Average Word Length:     ", avg_word_len)


if __name__ == "__main__":
    main()

  
