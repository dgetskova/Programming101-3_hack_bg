import copy


def count_words(arr):
    to_return = {}
    for x in arr:
        to_return[x] = arr.count(x)
    return to_return


def unique_words_count(arr):
    only_diff = set(arr)
    return len(only_diff)


def nan_expand(times):
    to_return = ""
    if times == 0:
        return to_return
    begin = "Not a "
    end = "Nan"
    for a in range(1, times + 1):
        to_return += begin
    to_return += end
    return to_return


def iterations_of_nan_expand(expanded):
    begin = "Not a "
    expected_len = expanded.count(begin) * len(begin) + len('NaN')
    return expected_len == len(expanded)

# do tuk


def is_prime(n):
    n = abs(n)
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def can_divide(e, elem):
    return e % elem == 0


def prime_factorization(num):
    num_copy = num
    all_prime = []

    for n in range(2, num + 1):

        if is_prime(n) and can_divide(num_copy, n):
            divisor = n
            times = 1
            num_copy /= n

            while can_divide(num_copy, n):
                num_copy /= n
                times += 1
            all_prime.append((divisor, times,))

    return all_prime


def group(obj):
    to_return = []
    to_return.append([obj[0]])
    index_elem_before = 0
    index_list = 0

    for x in obj[1:]:

        if x == obj[index_elem_before]:
            to_return[index_list].append(x)
        else:
            index_list += 1
            to_return.append([x])

        index_elem_before += 1

    return to_return


def max_consecutive(items):
    to_groups = group(items)
    max_size = len(to_groups[0])

    for i in to_groups:
        if len(i) > max_size:
            max_size = len(i)

    return max_size


def groupby(func, seq):
    result = {}

    for elem in seq:
        if func(elem) in result:
            result[func(elem)].append(elem)
        else:
            result[func(elem)] = [elem]
    return result


# immutable
def count_of_consist(number_original, divisor):
    count = 0
    number = copy.deepcopy(number_original)
    while number > 1:
        if number % divisor == 0:
            count += 1
            number /= divisor
        else:
            return count
    return count


def prepare_meal(number):
    consist_three = count_of_consist(number, 3)
    consist_five = count_of_consist(number, 5)
    if consist_three == 0 or consist_five == 0:
            return consist_three*" three" + consist_five*' five'
    return consist_three*" three" + ' and' + consist_five*' five'
