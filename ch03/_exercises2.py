def example1(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def example2(n):
    p = 1
    for i in range(1, 2 * n + 1):
        p *= i
    return p


def example3(n):
    p = 1
    for i in range(1, int(n**2) + 1):
        p *= i
    return p


def example4(n):
    sum = 0
    for i in range(1, 2 * n + 1):
        for j in range(1, i + 1):
            sum += i
    return sum


def example5(n):
    sum = 0
    for i in range(1, int(n**2) + 1):
        for j in range(1, i + 1):
            sum += i
    return sum
