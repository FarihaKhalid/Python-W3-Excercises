"""
rows = 3
col = 4
two_d_list = []
for i in range(rows):
    row = []
    for j in range(col):
        row.append(j)
    two_d_list.append(row)
print(two_d_list)
print(two_d_list[1][2])
"""
"""
rows = 3
col = 4

two_d_list = []

for i in range(rows):
    row = []
    for j in range(col):
        row.append(i * 10 + j)
    two_d_list.append(row)
print(two_d_list)
print(type(two_d_list))
"""
"""
row = 2
column = 2
my_two_d = [[len(row)], [len(column)]]
#my_two_d[0][1] = 111
#my_two_d[0][2] = 222

print(my_two_d)
#print(my_two_d[0][1])
#print(my_two_d[0][2])
"""
"""
def search_element(list_2D,target):
    bol_ans = False
    for i in range(len(list_2D)):
        for j in range(len(list_2D[i])):
            s = list_2D[i][j]
            if s == target:
                bol_ans = True
                return i , j
    if not bol_ans:
        return -1, -1

result = search_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1000)
print(result)
"""
"""
def sum_of_rows(list_2D):
    list = []
    for i in range(len(list_2D)):
        sum0 = 0
        for j in range(len(list_2D[i])):
            sum0 = sum0 + list_2D[i][j]
        list.append(sum0)
    return list

result = sum_of_rows([[1, 2], [3], [], [4, 5, 6]])
print(result)
"""
def add_matrices(matrix1, matrix2):
    list = []
    check1 = len(matrix1)
    check2 = len(matrix2)
    if check1 > 0 and check2 > 0:
        for i in range(len(matrix1)):
            row_result = []
            for j in range(len(matrix1[i])):
                sum0 = matrix1[i][j] + matrix2[i][j]
                row_result.append(sum0)
            list.append(row_result)
    return list
res = add_matrices([[1, 2], [3, 4]] , [[1, 1], [1, 1]])
print(res)