from colorama import Fore
from experta import *

welcome_message = """
Hi! I am your car Diagnosis Expert system, I am here to help you find out what the issue with your vehicle is.\n
For that you'll have to answer a few questions before we can determine where the issue is coming from.\n \n
Did you see any of the following signs in your car?")
"""

def input_yes_no(question):
    """
    Ask a yes/no question via input() and return their answer.
    "question" is a string that is presented to the user.
    The "answer" return value is "yes" or "no".
    """
    valid = {"yes", "no"}

    while True:
        print(Fore.WHITE, "\n"+ question + "\n")
        answer = input().strip().lower()
        if answer in valid:
            return answer
        else:
            print(Fore.RED, "\nPlease respond with 'yes' or 'no'.\n")