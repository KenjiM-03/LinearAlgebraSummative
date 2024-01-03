import numpy
import numpy as np

def generate_matrix():
    while True:
        Rows = int(input("Give the number of rows: "))
        Columns = int(input("Give the number of columns: "))

        print("Please write the elements of the matrix in a single line and separated by a space: ")
        elements = list(map(int, input().split()))
        return np.array(elements).reshape(Rows, Columns)

def add_matrices():
    while True:
        print("Generate Matrix 1")
        matrix1 = generate_matrix()
        print("Matrix 1:")
        print(matrix1)

        print("Generate Matrix 2")
        matrix2 = generate_matrix()
        print("Matrix 2:")
        print(matrix2)

        if matrix1.shape == matrix2.shape:
            break  # Exit the loop if matrices have the same dimensions
        else:
            print("Matrices must have the same dimensions. Please try again.")

    print("Matrix 1:")
    print(matrix1)
    print("+")
    print("Matrix 2:")
    print(matrix2)

    sum_matrix = numpy.add(matrix1,matrix2)  # Perform addition within the function
    return sum_matrix  # Return the sum matrix
    #exit()
def sub_matrices():
    while True:
        print("Generate Matrix 1")
        matrix1 = generate_matrix()
        print("Matrix 1:")
        print(matrix1)

        print("Generate Matrix 2")
        matrix2 = generate_matrix()
        print("Matrix 2:")
        print(matrix2)

        if matrix1.shape == matrix2.shape:
            break  # Exit the loop if matrices have the same dimensions
        else:
            print("Matrices must have the same dimensions. Please try again.")

    print("Matrix 1:")
    print(matrix1)
    print("*")
    print("Matrix 2:")
    print(matrix2)


    diff_matrix = numpy.subtract(matrix1,matrix2)  # Perform addition within the function
    return diff_matrix  # Return the sum matrix
    #exit()
def multiply_matrices():
    while True:
        print("Generate Matrix 1")
        matrix1 = generate_matrix()
        print("Matrix 1:")
        print(matrix1)

        print("Generate Matrix 2")
        matrix2 = generate_matrix()
        print("Matrix 2:")
        print(matrix2)

        if matrix1.shape[1] == matrix2.shape[0]:
            break  # Exit the loop if matrices have the same dimensions
        else:
            print("Matrices must have the same dimensions. Please try again.")

    print("Matrix 2:")
    print(matrix2)
    print("Matrix 1:")
    print(matrix1)
    print("-")
    print("Matrix 2:")
    print(matrix2)



    prod_matrix = np.dot(matrix1,matrix2)
    return prod_matrix
    #exit()

def main():
    while True:
        print("Choose a function:")
        print("1. Generate Matrix")
        print("2. Add Matrices")
        print("3. Subtract Matrices")
        print("4. Multiply Matrices")
        print("5. Exit")
        choice = input("Enter the number of the function you want to use: ")
        if choice == "1":
            matrix = generate_matrix()
            print("Generated Matrix: ")
            print(matrix)
        elif choice == "2":
            sum_matrix = add_matrices()  # Store the returned matrix
            print("Sum of the matrices:")
            print(sum_matrix)  # Print the sum matrix
        elif choice == "3":
            diff_matrix = sub_matrices()
            print("Difference of matrices:")
            print(diff_matrix)
        elif choice == "4":
            prod_matrix = multiply_matrices()
            print("Product of matrices:")
            print(prod_matrix)
        elif choice == "5":
            exit()
        else:
            print("Invalid choice. Please enter a valid number.")


if __name__ == "__main__":
    main()
