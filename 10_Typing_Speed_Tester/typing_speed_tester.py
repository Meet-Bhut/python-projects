import random
import time
from colorama import Fore, Style,init
init()
from itertools import zip_longest

def choose_difficulty():
    while True:
        print("==========MENU==========")
        print("""
    1.Easy
    2.Medium
    3.Hard
    4.Exit
    """)
        try:
            choice=int(input("Enter the Difficulty level: "))
            if choice < 1 or choice > 4:
                print("Enter a number between 1 and 4")
                continue
        except ValueError:
            print("Please enter a valid number")
            continue
        if choice == 1:
            return "easy"
        elif choice == 2:
            return "medium"
        elif choice == 3:
           return "hard"
        elif choice == 4:
            return "exit"

sentences = {
    "easy": [
        "Python is fun.",
        "Practice every day.",
        "Coding is easy.",
        "Learn Python daily.",
        "Functions save time.",
        "Loops repeat tasks.",
        "Lists store values.",
        "Coding improves skills.",
        "Errors help learning.",
        "Programs solve problems."
    ],

    "medium": [
        "Functions help organize code.",
        "Practice makes a programmer better.",
        "Python supports object oriented programming.",
        "Dictionaries store key value pairs.",
        "Exception handling prevents crashes.",
        "File handling stores information permanently.",
        "Problem solving improves programming skills.",
        "Debugging is an important skill.",
        "Algorithms make programs efficient.",
        "Consistent practice builds confidence."
    ],

    "hard": [
        "Exception handling improves software reliability and stability.",
        "Object oriented programming increases maintainability and reusability.",
        "Consistent practice develops strong problem solving abilities.",
        "Data structures organize information efficiently in memory.",
        "Abstraction helps reduce the complexity of large applications.",
        "Python provides powerful libraries for data analysis and automation.",
        "Writing clean code improves readability and maintainability.",
        "Efficient algorithms reduce execution time and memory usage.",
        "Software testing helps identify bugs before deployment.",
        "Understanding complexity analysis improves algorithm selection."
    ]
}

def get_sentence(difficulty):
    sentence_list=sentences[difficulty]
    return random.choice(sentence_list)

def start_test(sentence):
    print("\nType the following sentence:\n")
    print(sentence)
    print()
    input("Press Enter when ready...")
    start=time.time()
    typed_text = input("Type here: ")
    end=time.time()
    time_taken=end-start
    return typed_text,time_taken

def calculate_wpm(typed_text, time_taken):
    text_list=typed_text.split()
    return round(len(text_list) * 60 / time_taken, 2)

def calculate_accuracy(original, typed):
    correct=0
    for o,t in zip_longest(original, typed, fillvalue=""):
        if o==t:
            correct+=1
    total=max(len(original),len(typed))
    return round(correct / total * 100, 2)

def show_result(original, typed):
    for o,t in zip_longest(original,typed,fillvalue=""):
        if o==t:
            print(Fore.GREEN + t+ Style.RESET_ALL, end="")
        else:
            print(Fore.RED + t+ Style.RESET_ALL, end="")


while True:
    difficulty = choose_difficulty()
    if difficulty == "exit":
        print("Exiting...")
        break

    sentence = get_sentence(difficulty)
    typed_text, time_taken = start_test(sentence)
    wpm = calculate_wpm(typed_text, time_taken)
    accuracy = calculate_accuracy(sentence, typed_text)

    print("\n========== RESULTS ==========")
    print(f"Difficulty : {difficulty.title()}")
    print(f"Time Taken : {time_taken:.2f} seconds")
    print(f"WPM        : {wpm}")
    print(f"Accuracy   : {accuracy}%")
    print("\n" + "="*30)
    print("Typing Analysis")
    print("="*30)
    print("\nOriginal Sentence:")
    print(sentence)

    print("\nYour Input:")
    print(typed_text)

    print("\nTyping Analysis:")
    show_result(sentence, typed_text)
    print("\n" + "=" * 30 + "\n")