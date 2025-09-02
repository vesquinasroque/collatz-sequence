#!/usr/bin/env python3
"""
Collatz Sequence Generator
--------------------------
A basic Python script that generates the Collatz sequence
for a number entered by the user.
"""

import logging


def setup_logging(log_file: str = "log.txt") -> None:
    """Configure logging settings."""
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def collatz(number: int) -> int:
    """
    Return the next number in the Collatz sequence.

    Args:
        number (int): Current number in the sequence.

    Returns:
        int: Next number in the sequence.
    """
    if number % 2 == 0:
        return number // 2
    return 3 * number + 1


def main() -> None:
    """Main entry point of the program."""
    setup_logging()

    try:
        user_input = int(input("Type a positive integer: "))
        if user_input <= 0:
            print("⚠️ The number must be positive.")
            return

        logging.info("User entered: %s", user_input)

        number = user_input
        print("Collatz sequence:", end=" ")

        while number != 1:
            print(number, end=" ")
            number = collatz(number)

        print(1)  # last number is always 1

    except ValueError:
        print("⚠️ Please enter a valid integer.")
        logging.error("Invalid input: not an integer.")


# run the program directly
main()
