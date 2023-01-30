"""
Goals : Return missing value in range list of number 
"""

def missing_num(number):

    miss_val = []
    min_num = min(number)
    max_num = max(number)
   
    for i in range(min_num, max_num):
        if i not in number:
            miss_val.append(i)

    return miss_val


number = [2, 4, 4, 5, 4, 6, 7, 8, 10, 16, 17, 18, 20]
print(missing_num(number))
