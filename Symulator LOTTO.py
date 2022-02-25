# Symulator LOTTO
import random


RANGE = 6


def check_presence(number, list_of_numbers):
    """
    Returns True if number a is present in list b, otherwise returns False.
    :return: boolean
    """

    if number in list_of_numbers:
        return True
    else:
        return False


def sort_n_print(a):
    """
    Sorts input list a and prints it out as a string
    :return: None
    """

    sort_list = sorted(a)
    print(" ".join([str(x) for x in sort_list]))


def get_numbers():
    """
    Asks user for set of numbers. Input is revised if:
    * it is a number,
    * given numbers are unique,
    * are in set range.
    Then returns sorted list of passed numbers.
    :return: list
    """

    t = []
    i = 1
    while i <= RANGE:
        try:
            num = int(input(f'Please enter {i} number out of {RANGE}:\n'))
        except ValueError:
            print("Given value is not a number!")
            continue

        if num in range(1, 50):
            if not check_presence(num, t):
                t.append(num)
                i += 1
            else:
                print("Number is already chosen. Please pick another number")
        else:
            print("Picked number is out of range (1-49)")
            continue
    return t


def draw_numbers():
    """
    Draw random, unique numbers and returns them as list of sorted integers.
    Quantity of numbers is equal to set range.
    :return: list: list of sorted integers
    """
    t = []

    while len(t) < len(range(RANGE)):
        drawn_number = random.randint(1, 49)
        if not check_presence(drawn_number, t):
            t.append(drawn_number)
        else:
            continue
    return t


def check_numbers(input_list, reference_list):
    """
    Checks how much of numbers given by user are in match with randomly drawn numbers
    :return:
    """

    counter = 0
    for i in input_list:
        for element in reference_list:
            if i == element:
                counter += 1
            else:
                continue
    return counter


def lotto_game():
    """
    Game of LOTTO. Choose set of numbers and check if you hit jackpot
    :return: Victory prompt
    """

    input_numbers = get_numbers()
    drawn_numbers = draw_numbers()
    print("-" * 30)
    print("Your numbers are:")
    sort_n_print(input_numbers)
    print(" " * 30)
    print("Drawn numbers are:")
    sort_n_print(drawn_numbers)
    print(" " * 30)
    i = check_numbers(input_numbers, drawn_numbers)
    print(f'You got {i} right')


if __name__ == "__main__":
    lotto_game()
