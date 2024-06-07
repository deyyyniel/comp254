import time
import random


def unique1(S):
    for j in range(len(S)):
        for k in range(j + 1, len(S)):
            if S[j] == S[k]:
                return False
    return True


def unique2(S):
    temp = sorted(S)
    for j in range(1, len(temp)):
        if S[j - 1] == S[j]:
            return False
    return True


def measure_time(func, S):
    start = time.time()
    func(S)
    end = time.time()
    return end - start


def find_max_n(func, max_time=1, initial_low=10**6, initial_high=10**8):
    low, high = initial_low, initial_high

    while low <= high:
        mid = (low + high) // 2
        S = [random.randint(10**6, 10**8) for _ in range(mid)]
        exec_time = measure_time(func, S)

        if exec_time < max_time:
            low = mid + 1
        else:
            high = mid - 1

    return high


max_n_unique1 = find_max_n(unique1)
max_n_unique2 = find_max_n(unique2)

print(f"Maximum n for unique1: {max_n_unique1}")
print(f"Maximum n for unique2: {max_n_unique2}")
