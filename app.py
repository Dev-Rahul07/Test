"""Small examples of intentional logic bugs for debugging practice."""


def largest_number(numbers):
    # Bug: this returns 0 when every number in the list is negative.
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    return largest


def apply_discount(price, discount_percent):
    # Bug: percent should be divided by 100 before calculating the discount.
    return price - (price * discount_percent)


if __name__ == "__main__":
    print("Largest:", largest_number([-8, -3, -12]))  # Incorrectly prints 0
    print("Discounted price:", apply_discount(100, 20))  # Incorrectly prints -1900