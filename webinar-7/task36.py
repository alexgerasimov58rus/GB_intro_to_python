
def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            cell = operation(row, col)
            print(cell, end='\t')
        print()

print_operation_table(lambda x, y: x * y, 6, 8)
print()           
print_operation_table(lambda x, y: x + y)  