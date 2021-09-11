def matrix_multiplication(a, b):
    columns_a = len(a[0])
    rows_a = len(a)
    columns_b = len(b[0])
    rows_b = len(b)

    # first a row by first b column becomes single c value
    # which means a number of rows by b number of columns
    # matrix = [rows x columns]
    # a = [m x n]; b = [n x p]
    # [m x n] x [n x p] = [m x p]
    # 
    result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
    if columns_a == rows_b:
        for row in range(rows_a):
            for col in range(columns_b):
                sum = 0
                for k in range(columns_a):
                    sum += a[row][k] * b[k][col]
                result_matrix[row][col] = sum
        return result_matrix
    else:
        print("error! the columns of the first matrix must be equal with the rows of the second matrix")
        return None