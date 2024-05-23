"""
A simple script to demonstrate input and output in Python.
"""


def process_input(input):
    """
    Process the user input and return a formatted string.

    Args:
        user_input (str): The input string from the user.

    Returns:
        str: A formatted string.
    """
    return f"You entered: {input}"


if __name__ == "__main__":
    user_input = input("Please enter something: ")
    output = process_input(user_input)
    print(output)
