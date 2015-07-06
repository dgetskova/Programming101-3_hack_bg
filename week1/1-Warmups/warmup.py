def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


def sum_of_digits(n):
    return sum(to_digits(n))


def to_digits(n):
    return [int(x) for x in str(n)]


def fac_to_digits(n):
    return sum([fact(x) for x in to_digits(n)])


def sum_of_divisors(n):
    result = 0
    devisor = n
    while devisor >= 1:
        if n % devisor == 0:
            result += devisor
        devisor -= 1
    return result


def is_prime(n):
    return n + 1 == sum_of_divisors(n)


def palindrome(obj):
    return str(obj) == str(obj)[::-1]


def count_digits(n):
    return sum([1 for x in to_digits(n)])


def to_number(obj):
    sumy = 0

    for x in obj:
        digits_count = count_digits(x)
        sumy = sumy + (10 ** digits_count) + int(x)

    return sumy


def count_vowels(str):
    volews = "aeiouyAEIOUY"
    count = 0
    for x in str:
        if x in volews:
            count += 1
    return count


def char_histogram(string):
    to_return = {}

    for x in string:
        to_return[x] = string.count(x)

    return to_return


def p_score(n):
    reversed_n = str(n)[::-1]

    if str(n) == reversed_n:
        return 1

    to_return = n + int(reversed_n)
    return 1 + p_score(to_return)


def is_increasing(seq):
    previous = seq[0]

    for x in seq[1:]:
        if previous > x:
            return False
        previous = x

    return True


def next_hack(num):
    num += 1

    if str(bin(num))[2:] == str(bin(num))[::-1][:-2] and \
            str(bin(num)).count('1') % 2 is not 0:
        return num
    return next_hack(num)
