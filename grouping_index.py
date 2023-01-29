"""
Goals : Group list value by the same index 
"""

# 1

inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
len_list = len(inputLists)

result = [[inputLists[x][0] for x in range(len_list)],
          [inputLists[x][1] for x in range(len_list)],
          [inputLists[x][2] for x in range(len_list)]]

print(result)

# 2

result2 = []
for i in range(len(inputLists)):
    new_list = []
    for j in range(len(inputLists[0])):
        new_list.append(inputLists[j][i])
    result2.append(new_list)

print(result2)
