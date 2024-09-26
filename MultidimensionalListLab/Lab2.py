import sys
from io import StringIO

test_input1 = """2
1, 2, 3
4, 5, 6
"""

test_input2 = """4
10, 33, 24, 5, 1
67, 34, 11, 110, 3
4, 12, 33, 63, 21
557, 45, 23, 55, 67
"""

sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input1)


rows = int(input())


# data_matrix = [[int(j) for j in input().split(', ')] for i in range(n)] # use comprehension

result_matrix = []
#prochitame matricata i napravo filtrirame
for el in range(rows):
    row_data = [int(el) for el in input().split(', ') if int(el)%2==0]
    result_matrix.append(row_data)

# even_matrix = []
#
# for row_index in range(len(result_matrix)):
#     even_matrix.append([])
#     for col_index in range(len(result_matrix[row_index])):
#         if result_matrix[row_index][col_index]%2==0:
#             even_matrix[row_index].append(result_matrix[row_index][col_index])
#
# 
#
#
#
#
# print(even_matrix)
print(result_matrix)






