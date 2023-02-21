def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# print(factorial(4))


def non_negative_sum(n):
    if n == 1:
        return 1
    return n + non_negative_sum(n-1)


# print(non_negative_sum(475))


def no_of_grid_paths(n, m):
    if m == 1 or n == 1:
        return 1
    return no_of_grid_paths(n, m-1) + no_of_grid_paths(n-1, m)


print(no_of_grid_paths(3, 3))
