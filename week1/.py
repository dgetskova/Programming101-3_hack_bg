import copy
from lec1 import to_digits


def sum_of_divisors(n):
    return sum([x for x in range(1, n + 1) if n % x == 0])

# print (sum_of_divisors(1000))


def is_prime(n):
    n = abs(n)
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

# print (is_prime(8))


def is_prime_hack(n):
    return n + 1 == sum_of_divisors(n)


def digit_from_number(number):
    result = []
    while number > 0:
        one = number % 10
        result.append(one)
        number //= 10
    return result

# print(digit_from_number(541))


def is_number_balanced(n):
    numbs = to_digits(n)
    half = len(numbs) // 2
    left_numbs = numbs[0:half]

    if len(numbs) % 2 == 0:
        right_numbs = numbs[half:]
    else:
        right_numbs = numbs[half + 1:]

    return sum(left_numbs) == sum(right_numbs)

# print(is_number_balanced(121))

def count_substrings(haystack, needle):
    return haystack.count(needle)

# print (count_substrings("babababa", "baba"))


def zero_insert(obj):
    result = []
    digits = to_digits(obj)

    start = 0
    end = len(digits)
    # print (start, end)
    result.append(digits[0])
    while start < end - 1:
        x = digits[start]
        y = digits[start + 1]

        if x == y or x + y == 10:
            result.append(0)

        result.append(y)
        # print (result)
        start += 1
        # print (start)

    str1 = ''.join(str(e) for e in result)
    print(str1)

# print (zero_insert(555555))


def sum_matrix(matr):
    result = 0
    print(matr)
    for row in matr:
        result += sum(row)
    print(result)
    return result


NEIGHBORS = [
    (-1, -1), (-1, 0), (-1, 1),  # up row
    (0, -1), (0, 1),  # the same row
    (1, -1), (1, 0), (1, 1)]  # next row


def within_bounds(matrix, at):
    if at[0] < 0 or at[1] < 0:
        return False

    if at[0] >= len(matrix) or at[1] >= len(matrix[0]):
        return False

    return True


def bomb(matrix, at):
    for n in NEIGHBORS:
        i = at[0] + n[0]
        j = at[1] + n[1]
        # print (within_bounds(matrix, (i, j)), i, j)
        if within_bounds(matrix, (i, j)):
            # print('                    chislo :: ', matrix[i][j])
            if matrix[i][j] <= matrix[at[0]][at[1]]:
                matrix[i][j] = 0
            else:
                matrix[i][j] -= matrix[at[0]][at[1]]
    return matrix


def matrix_bomb(matrix):
    result = {}

    i = 0
    for row in matrix:
        j = 0
        for col in matrix[0]:
            bombed = bomb(copy.deepcopy(matrix), (i, j))
            result[(i, j)] = sum_matrix(bombed)
            j += 1
        i += 1

    return result

# m = [[1, 2], [3, 4]]
# matrix_bomb(m)
