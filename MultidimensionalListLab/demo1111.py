matrix=[]

rows_count = 3
column_count = 2

for row_index in range(rows_count):
    row=[]
    for column_index in range(column_count):
        row.append(0)
    matrix.append(row)

print(matrix)

matrix2=[[0]*column_count for _ in range(rows_count)]
print(matrix2)