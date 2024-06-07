def example1(n):
    sum = 0  # O(1) - Initializing sum
    for i in range(1, n + 1):  # O(n) - Loop runs n times
        sum += i  # O(1) - Addition is a constant time operation
    return sum  # O(1) - Returning the sum
    # Overall Time Complexity: O(n)


def example2(n):
    p = 1  # O(1) - Initializing p
    for i in range(
        1, 2 * n + 1
    ):  # O(2n) - Loop runs 2n times (still O(n) in big-Oh notation)
        p *= i  # O(1) - Multiplication is a constant time operation
    return p  # O(1) - Returning the product
    # Overall Time Complexity: O(n)


def example3(n):
    p = 1  # O(1) - Initializing p
    for i in range(1, int(n**2) + 1):  # O(n^2) - Loop runs n^2 times
        p *= i  # O(1) - Multiplication is a constant time operation
    return p  # O(1) - Returning the product
    # Overall Time Complexity: O(n^2)


def example4(n):
    sum = 0  # O(1) - Initializing sum
    for i in range(
        1, 2 * n + 1
    ):  # O(2n) - Outer loop runs 2n times (still O(n) in big-Oh notation)
        for j in range(1, i + 1):  # O(i) - Inner loop runs i times
            sum += i  # O(1) - Addition is a constant time operation
    # Total time complexity for the nested loops is the sum of the series 1 + 2 + 3 + ... + 2n, which is O(n^2)
    return sum  # O(1) - Returning the sum
    # Overall Time Complexity: O(n^2)


def example5(n):
    sum = 0  # O(1) - Initializing sum
    for i in range(1, int(n**2) + 1):  # O(n^2) - Outer loop runs n^2 times
        for j in range(1, i + 1):  # O(i) - Inner loop runs i times
            sum += i  # O(1) - Addition is a constant time operation
    # Total time complexity for the nested loops is the sum of the series 1 + 2 + 3 + ... + n^2, which is O(n^4)
    return sum  # O(1) - Returning the sum
    # Overall Time Complexity: O(n^4)
