import math

def mean(numbers):
    """numbers = list or iterable"""
    n = len(numbers)
    sumation = sum(numbers)
    return sumation/n

def mode(numbers):
    num_len = dict()
    for number in numbers:
        # num_len[number] = num_len[number] + 1 if number in num_len else num_len[number] = 1
        if number in num_len:
            num_len[number] = num_len[number] + 1
        else:
            num_len[number] = 1

    num_len = {val: key for key, val in num_len.items()}
    """Write a function to return a tuple or set if there are more than one mode"""
    return num_len[max(num_len)]

def median(numbers):
    num_arr = list(numbers)
    num_arr.sort()
    num_len = len(num_arr)
    # mid_num = num_arr[num_len//2] if num_len%2 != 0 else mid_num = (num_arr[num_len/2] + num_arr[num_len/2 - 1])/2
    if num_len % 2 != 0:
        mid_num = num_arr[num_len // 2]
    else:
        mid_num = (num_arr[num_len // 2] + num_arr[num_len // 2 - 1]) / 2
    return mid_num


print(median((1, 5, 3, 9, 5, 6, 7)))
