"""Debugging practice: this average function has an intentional bug."""


def average(numbers):
    # Bug: integer division discards the fractional part.
    return sum(numbers) // len(numbers)


if __name__ == "__main__":
    values = [1, 2, 3, 4]
    print("Average:", average(values))  # Incorrectly prints 2 instead of 2.5
