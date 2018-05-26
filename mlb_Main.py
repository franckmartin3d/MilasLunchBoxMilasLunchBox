#Franck 21/05/2018
#MLB Main Menu

def main():
    print("""\n
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 *                                                                                       *
 *           _ _       _        __                  _         ___                        *
 *      /\/\ (_| | __ _( ___    / / _   _ _ __   ___| |__     / __\ _____  __            *
 *     /    \| | |/ _` |/ __|  / / | | | | '_ \ / __| '_ \   /__\/// _ \ \/ /            *
 *    / /\/\ | | | (_| |\__ \ / /__| |_| | | | | (__| | | | / \/  | (_) >  <             *
 *    \/    \|_|_|\__,_||___/ \____/\__,_|_| |_|\___|_| |_| \_____/\___/_/\_\            *
 *                                                                                       *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *



                                ___  ___
                                |  \/  |
                                | .  . | ___ _ __  _   _
                                | |\/| |/ _ | '_ \| | | |
                                | |  | |  __| | | | |_| |
                                \_|  |_/\___|_| |_|\__,_|


                                    1. Recepei

                                    2. Lunch Box

                                    3. Dinner

                                    4. Breakfast Fun

                                    5. Stats

                                    6. Requirements

                                    0. Exit



* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    """)

def ask_a_number(question, low, high):
    """Ask for a number within a range
    Input : Question, low number, high number
    Return: Response to question"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def menu_selected(response):
    if response == "1" :


    elif


def recepei_menu():
    print("Welcome to the Recepei Menu")


main()
ask_a_number("What menu item do you select?", 0, 6)
