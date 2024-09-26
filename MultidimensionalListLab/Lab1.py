


def read_matrix(is_test=False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]
    else:

        (rows_count, column_count) = map(int, input().split(', '))
        matrix = []
        for row_index in range(rows_count):
            row = list(map(int, input().split(', ')))
            matrix.append(row)
        return matrix


matrix = read_matrix()
matrix_sum = 0

for el in matrix:
    matrix_sum+=sum(el)

print(matrix_sum)









print(matrix)

