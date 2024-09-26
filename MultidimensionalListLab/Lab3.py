import sys
from io import StringIO

test_input1 = """2
1, 2, 3
4, 5, 6
"""

test_input2 = """3
10, 2, 21, 4
5, 20, 41, 9
6, 2, 4, 99
"""

sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input1)


n = int(input())


data_matrix = [[int(j) for j in input().split(', ')] for i in range(n)] # use comprehension

result_matrix = []

for el in data_matrix:
    for x in el:
        result_matrix.append(x)

# matrix=[]
# for i in range(3):
#     matrix.append([])
#     for j in range(2):
#         matrix[i].append(0)
#

# print(data_matrix)
print(result_matrix)