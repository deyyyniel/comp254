def example1(S):
    n = len(S)  # O(1) - Getting the length of S is a constant time operation
    total = 0  # O(1) - Initializing a variable is a constant time operation
    for j in range(n):  # O(n) - The loop runs n times
        total += S[
            j
        ]  # O(1) - Accessing an element and addition are constant time operations
    return total  # O(1) - Returning a value is a constant time operation


# Overall Time Complexity: O(n)


def example2(S):
    n = len(S)  # O(1) - Getting the length of S is a constant time operation
    total = 0  # O(1) - Initializing a variable is a constant time operation
    for j in range(
        0, n, 2
    ):  # O(n/2) - The loop runs n/2 times (still O(n) in big-Oh notation)
        total += S[
            j
        ]  # O(1) - Accessing an element and addition are constant time operations
    return total  # O(1) - Returning a value is a constant time operation


# Overall Time Complexity: O(n)


def example3(S):
    n = len(S)  # O(1) - Getting the length of S is a constant time operation
    total = 0  # O(1) - Initializing a variable is a constant time operation
    for j in range(n):  # O(n) - The outer loop runs n times
        for k in range(1 + j):  # O(j+1) - The inner loop runs (j+1) times
            total += S[
                k
            ]  # O(1) - Accessing an element and addition are constant time operations
    # The total time complexity for the nested loops is the sum of the series 1 + 2 + 3 + ... + n
    # which is O(n^2)
    return total  # O(1) - Returning a value is a constant time operation


# Overall Time Complexity: O(n^2)


def example4(S):
    n = len(S)  # O(1) - Getting the length of S is a constant time operation
    prefix = 0  # O(1) - Initializing a variable is a constant time operation
    total = 0  # O(1) - Initializing a variable is a constant time operation
    for j in range(n):  # O(n) - The loop runs n times
        prefix += S[
            j
        ]  # O(1) - Accessing an element and addition are constant time operations
        total += prefix  # O(1) - Addition is a constant time operation
    return total  # O(1) - Returning a value is a constant time operation


# Overall Time Complexity: O(n)


def example5(A, B):
    n = len(A)  # O(1) - Getting the length of A is a constant time operation
    count = 0  # O(1) - Initializing a variable is a constant time operation
    for i in range(n):  # O(n) - The outer loop runs n times
        total = 0  # O(1) - Initializing a variable is a constant time operation
        for j in range(n):  # O(n) - The middle loop runs n times
            for k in range(1 + j):  # O(j+1) - The inner loop runs (j+1) times
                total += A[
                    k
                ]  # O(1) - Accessing an element and addition are constant time operations
        # The total time complexity for the nested loops is O(n^2) for the j-loop and k-loop
        if B[i] == total:  # O(1) - Comparison is a constant time operation
            count += 1  # O(1) - Incrementing a variable is a constant time operation
    # The overall time complexity is O(n) * O(n^2) = O(n^3)
    return count  # O(1) - Returning a value is a constant time operation


# Overall Time Complexity: O(n^3)
