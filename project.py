import sys
from random import randrange
from pyfiglet import Figlet
import todo
import tictactoe
import exchange


def project():
    global thank_you
    thank_you = False
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "thanks":
            thank_you = True
            thanks()
    print("Welcome to my project! Available programs:")
    print("Tic-tac-toe, Todo List, Currency Exchange")
    print('Or to exit, type "exit"')
    while True:
        program = input("What would you like to use? ")
        valid_todo_list = [
            "todo list",
            "todo_list",
            "to do list",
            "to_do_list",
            "to-do list",
            "to-do_list",
        ]
        valid_tictactoe = ["tictactoe", "tic tac toe", "tic-tac-toe", "tic_tac_toe"]
        valid_exchange = [
            "currency exchange",
            "currency_exchange",
            "exchange",
            "money exchange",
            "money_exchange",
        ]
        if program.lower().strip() in valid_todo_list:
            todo.todo()
            break
        elif program.lower().strip() in valid_tictactoe:
            tictactoe.play()
            break
        elif program.lower().strip() in valid_exchange:
            exchange.converter_main()
        elif program.lower().strip() == "exit":
            exit_project()
        else:
            print("Invalid entry")
            continue


def exit_project():
    if thank_you == True:
        thanks()
    sys.exit("Thank you CS50! Goodbye!")


def continue_or_exit():
    while True:
        print("Go back to the main project or exit the program?")
        user_input = input("return / exit: ")
        if user_input.lower().strip() == "return":
            project()
            break
        elif user_input.lower().strip() == "exit":
            exit_project()
            break
        else:
            print('Must input "return" or "exit"')
            continue


def thanks():
    figlet = Figlet()
    font_list = figlet.getFonts()
    font_name = None
    try:
        font_name = sys.argv[2].lower()
    except IndexError:
        pass
    if font_name not in font_list:
        font_name = None
    if not font_name:
        font_name = font_list[randrange(0, len(font_list))]
    figlet.setFont(font=font_name)
    print(figlet.renderText("Thank You"))
    print(figlet.renderText("  CS50!  "))


if __name__ == "__main__":
    project()
