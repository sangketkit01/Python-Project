import math
import sympy as sp
import scipy.stats as stats
from typing import Tuple


class Calculator :
    def calculate(self, expression: str) -> int  :
        try:
            result = eval(expression)
            return result
        except ZeroDivisionError:
            raise ZeroDivisionError("Can not divisible by 0")


class Calculus:
    def limit(self, f, x_value, a=0) -> any:
        x = sp.symbols('x')
        f = sp.sympify(f)
        f_substituted = f.subs(x, x_value)
        result = sp.limit(f_substituted, x, a) 
        return result   

    def differential(self, f) -> any:
        x = sp.symbols('x')
        x = sp.diff(f, x)
        return x

    def integral(self, f=0) -> str:
        x = sp.symbols('x')
        result = sp.integrate(f, x)
        return str(result) + ' + C'

    def areaIntegral(self, f=0, a=0, b=0) -> float:
        x = sp.symbols('x')
        result = sp.integrate(f, (x, a, b))
        return result


class Base_number:
    def toTwo(self, x=0) -> str:
        result = bin(x)
        return result.replace("0b", "")

    def toTen(self, x=0) -> int:
        result = int(x)
        return result 

    def toOct(self, x=0) -> str:
        result = oct(x)
        return result.replace("0o", "")

    def toHex(self, x=0) -> str:
        result = hex(x)
        return result.replace("0x", "")


class Statistic:
    def summation(self, x: str) -> float:
        sum = 0
        for i in x.split():
            sum += float(i)
        return sum

    def findAverage(self , x: str) -> float or str:
        memberX = 0
        sumX = 0
        for i in x.split():
            sumX += float(i)
            memberX += 1
        try:
            average = sumX / memberX
        except ZeroDivisionError:
            return "There's no member"
        return average

    def findMedian(self, n: str) -> float or int:
        sort_list = sorted([int(x) for x in n.split()])  
        member = len(sort_list)
        try:
            if member % 2 != 0:
                median = sort_list[((member + 1) // 2) - 1]
            else:
                median = (sort_list[(member // 2) - 1] +
                          sort_list[(member // 2)]) / 2
        except IndexError:
            return "You ran out of range"
        return median

    def findRange(self, n: str) -> float:
        number = [int(x) for x in n.split()]
        Max = max(number)   
        Min = min(number) 
        Qrange = Max - Min   
        return Qrange  

    def findVariance(self, x: str) -> Tuple[float, float] or str:
        Average = 0
        sumX = 0
        memberX = 0
        for i in x.split():
            sumX += float(i)
            memberX += 1
        try:
            Average = sumX / memberX
        except ZeroDivisionError:
            return "There's no member"

        for i in x.split():
            sumX += ((float(i) - Average) ** 2)
        try:
            variance = sumX / memberX
        except ZeroDivisionError:
            return "Can not divide by zero"
        sd = math.sqrt(variance) 
        return "{:.5f}".format(variance), "{:.5f}".format(sd)

    def findCnr(self, n: int, r: int) -> float or int:
        sumN = 1
        sumR = 1
        sumNR = 1
        for i in range(1, n + 1):
            sumN *= i
        for i in range(1, r + 1):
            sumR *= i
        for i in range(1, (n - r) + 1):
            sumNR *= i
        try:
            Cnr = sumN / (sumR * sumNR)
        except ZeroDivisionError:
            return "Can not divide by zero"
        return Cnr

    def findPnr(self, n=0, r=0) -> float or int:
        sumN = 1
        sumNR = 1
        for i in range(1, n + 1):
            sumN *= i
        for i in range(1, (n - r) + 1):
            sumNR *= i

        try:
            Pnr = sumN / sumNR
        except ZeroDivisionError:
            return "Can not divide by zero"
        return Pnr

    def findPnorm(self, x: float, mean: float, variance: float, n: int) -> float:
        std = variance**0.5
        if n >= 30:     
            result = stats.norm.cdf(x=n, loc=mean, scale=std)
        else:
            result = stats.norm.cdf(x, loc=mean, scale=std)
        return result


class Matrix:
    def plusMatrix(self, a: str, b: str) -> list[int] or str:
        newMatrix = []
        matrixA = a.split()
        matrixB = b.split()
        if len(matrixA) == len(matrixB) :
            for i in range(len(matrixA)):
                newMatrix.append(int(matrixA[i])+int(matrixB[i]))
            return newMatrix
        else:
            return "Two matrix must have the same dimension"

    def scale_matrix(self):
        # User input Rows and columns
        Row = int(input("Enter Rows: "))
        Column = int(input("Enter Columns: "))

        # Make a matrix and assign numbers into matrix
        matrix = []
        for i in range(Row):
            row = []
            for j in range(Column):
                number = float(input("Enter element of matrix : "))
                row.append(number)
            matrix.append(row)

        # Find MaxValue and MinValue in the matrix
        MaxValue = float('-inf')
        MinValue = float('inf')

        for i in range(Row):
            for j in range(Column):
                if matrix[i][j] > MaxValue:
                    MaxValue = matrix[i][j]
                if matrix[i][j] < MinValue:
                    MinValue = matrix[i][j]

        # Scaling into a 0-1 matrix
        scaled_matrix = []
        for i in range(Row):
            scaled_row = []
            for j in range(Column):
                scale = (matrix[i][j] - MinValue) / (MaxValue - MinValue)
                scaled_row.append(scale)
            scaled_matrix.append(scaled_row)

        # Print the scaled matrix
        print(f"{'='*35}")
        print("Result : ")
        for i in range(Row):
            for j in range(Column):
                print(f"{scaled_matrix[i][j]:.4f}", end=" ")
            print()
        print(f"{'='*35}")

    def multiply_matrix(self):

        # Input matrix dimensions
        rowsA = int(input("Enter the number of rows in the first matrix: ")) 
        colsA = int(input("Enter the number of columns in the first matrix: ")) 

        rowsB = int(input("Enter the number of rows in the second matrix: ")) 
        colsB = int(input("Enter the number of columns in the second matrix: ")) 

        try:
            assert colsA == rowsB
        except AssertionError:
            print("Matrices cannot be multiplied!")
            return None

        # Input elements of matrix A
        matrixA = []
        print("Enter elements of matrix A:")
        for i in range(rowsA):
            row = []
            for j in range(colsA):
                row.append(float(input()))
            matrixA.append(row)

        # Input elements of matrix B
        matrixB = []
        print("Enter elements of matrix B:")
        for i in range(rowsB):
            row = []
            for j in range(colsB):
                row.append(float(input()))
            matrixB.append(row)

        resultMatrix = [[0 for _ in range(colsB)] for _ in range(rowsA)]

        for i in range(rowsA):
            for j in range(colsB):
                for k in range(colsA):
                    resultMatrix[i][j] += matrixA[i][k] * matrixB[k][j]

        print(f"{'='*35}")
        print("Result matrix:")
        for row in resultMatrix:
            print(row)
        print(f"{'='*35}")

    def inverse_matrix(self):

        matrix_inverse = []

        for i in range(2): 
            matrix = []
            for j in range(2):
                matrix.append(int(input("Enter the elements of matrix : ")))
            matrix_inverse.append(matrix)

        newMatrix = [[matrix_inverse[-1][-1], -matrix_inverse[0][1]],
                     [-matrix_inverse[1][0], matrix_inverse[0][0]]]

        for i in newMatrix:
            print(i)
