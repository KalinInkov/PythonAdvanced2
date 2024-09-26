import sys
from io import StringIO

test_input1 = """3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
"""

test_input2 = """3, 3
1 2 3
4 5 6
7 8 9
"""

sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input1)

row, col = [int(x) for x in input().split(', ')]

matrix = []

for i in range(row):
    row_data = [int(x) for x in input().split(' ')]
    matrix.append(row_data)

for col_index in range(col):
    col_sum = 0
    for row_index in range(row):
        col_sum+=matrix[row_index][col_index]

    print(col_sum)

print(matrix)

