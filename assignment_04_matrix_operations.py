# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================


def read_matrix(rows, cols, name="Matrix"):
    """Helper function to read a matrix from user input line by line."""
    matrix = []
    print(f"\nEnter elements for {name} ({rows}x{cols}):")
    for i in range(rows):
        while True:
            row_str = input(f"Enter row {i + 1}: ").strip().split()
            if len(row_str) != cols:
                print(f"Error: Please enter exactly {cols} numbers separated by spaces.")
                continue
            try:
                row = [float(x) if '.' in x else int(x) for x in row_str]
                matrix.append(row)
                break
            except ValueError:
                print("Error: Invalid input. Please enter numeric values only.")
    return matrix


def display_matrix(matrix):
    """Helper function to print a matrix in a neat grid format."""
    if not matrix:
        return
    for row in matrix:
        print(" ".join(f"{val:>5}" for val in row))
    print()


# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
def transpose_matrix(matrix):
    """
    Computes the transpose of an M x N matrix.
    Returns an N x M matrix where rows become columns.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize an N x M matrix filled with zeros
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Fill transposed matrix using nested loops
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed


# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
def add_matrices(matrix_a, matrix_b):
    """
    Computes the element-wise sum of two M x N matrices.
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    # Initialize M x N result matrix filled with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Compute sum using nested loops
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
            
    return result


# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
def multiply_matrices(matrix_a, matrix_b):
    """
    Computes the matrix product A (M x N) * B (N x P).
    Returns an M x P result matrix.
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    # Initialize M x P result matrix filled with zeros
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    # Compute product using nested loops
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
                
    return result


# =============================================================================
# MAIN PROGRAM
# =============================================================================
def main():
    print("=== PART A: MATRIX TRANSPOSE ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    
    mat = read_matrix(m, n, "Original Matrix")
    print("\nOriginal Matrix:")
    display_matrix(mat)
    
    transposed = transpose_matrix(mat)
    print("Transposed Matrix:")
    display_matrix(transposed)
    
    print("-" * 40)
    print("=== PART B: MATRIX ADDITION ===")
    m_b = int(input("Enter number of rows: "))
    n_b = int(input("Enter number of columns: "))
    
    mat1 = read_matrix(m_b, n_b, "Matrix 1")
    mat2 = read_matrix(m_b, n_b, "Matrix 2")
    
    sum_mat = add_matrices(mat1, mat2)
    print("\nSum Matrix:")
    display_matrix(sum_mat)
    
    print("-" * 40)
    print("=== PART C: MATRIX MULTIPLICATION ===")
    m_c = int(input("Enter rows for Matrix A: "))
    n_c = int(input("Enter columns for Matrix A (and rows for Matrix B): "))
    p_c = int(input("Enter columns for Matrix B: "))
    
    mat_a = read_matrix(m_c, n_c, "Matrix A")
    mat_b = read_matrix(n_c, p_c, "Matrix B")
    
    prod_mat = multiply_matrices(mat_a, mat_b)
    print("\nProduct Matrix (A x B):")
    display_matrix(prod_mat)


if __name__ == "__main__":
    main()

#