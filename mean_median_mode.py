"""
Goals : Calculate mean median and mode from list of number   
"""

def find_mean(list_number: list):
    total = 0
    for i in list_number:
        total += i

    return round(total/len(list_number), 2)


def find_median(list_number: list):

    list_number.sort()
    if len(list_number) % 2 == 0:
        m1 = list_number[len(list_number)//2]
        m2 = list_number[len(list_number)//2-1]
        return (m1 + m2) / 2

    else:
        return list_number[len(list_number)//2]


def find_mode(list_number: list):

    num_freq = {}
    result = set()
    for i in list_number:
        num_freq.setdefault(i, 0)
        num_freq[i] += 1

    max_freq = max(num_freq.values())
    for key, value in num_freq.items():
        if value == max_freq:
            result.add(key)

    return result


number = [20, 12, 16, 20, 12, 30, 16, 25, 23, 24, 16, 23, 20, 17]

print("Mean : ", find_mean(number))
print("Median : ", find_median(number))
print("Mode : ", find_mode(number))
