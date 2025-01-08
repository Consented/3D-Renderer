# Matrix Addition - Adds 2 matrices together

def addition(A,B):
    # Matrices are added by:
    # 1) Comparing their size is equal to ensure addition is possible
    # 2) Defining the size of the resultant matrix using the size of Matrix A
    # 3) Adding each value of Matrix A and B together and set it to the respective value of the resultant matrix 

    if len(A) == len(B) and len(A[0]) == len(B[0]): # Ensures Matrices A and B are of the same size
        resultant = [[0 for i in range(len(A[0]))] for i in range(len(A))]
        
        for i in range(len(resultant)): # Need to get location of each matrix value (row)
            for j in range(len(resultant[0])): # (Column)
                resultant[i][j] = A[i][j] + B[i][j]
        return resultant
    else:
        return "Error: Matrices can not be added" 
        
# Matrix Multiplication - Multiplies 2 matrices together
def multiplication(A,B):
    # Matrices are multiplied by:
    # 1) Ensuring their size is able to correctly multiply
    # 2) Defininging the size of the resultant Matrix
    # 3) For each value in the resultant Matrix, loop through the number of neccesary additions
    # 4) For each addition use the loop iteration and value position using the equation 

    if len(A[0]) == len(B): # Ensure Matrices are same size
        resultant = [[0 for i in range(len(B[0]))] for i in range(len(A))]
        print(resultant)

        for i in range(len(resultant)): # Need to get location of Matrix values (row)
            for j in range(len(resultant[0])): # (column)
                for k in range(len(A[0])): # Must be A and not resultant this can be seen in the case of Matrix 2x2 multiplied by 2x1
                    resultant[i][j] += A[i][k] * B[k][j] 

        return resultant
    else:
        return "Error: Matrices can not be multiplied"


A = [
    [0,1],
    [1,0]
]
B = [
    [1,1],
    [1,1]
]
print(addition(A,B))

A = [
    [1, 0],
    [0,-1]
]
B = [
    [275],
    [275]
]

print(multiplication(A,B))