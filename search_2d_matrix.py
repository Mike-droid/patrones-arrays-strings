from typing import List

def searchMatrix(matriz: List[List[int]], objetivo: int) -> bool:
    m = len(matriz)
    n = len(matriz[0])
    left = 0
    right = (m*n) - 1
    #* easy way
    while left <= right:
        k = (left + right) // 2
        row = k // n
        col = k % n

        if matriz[row][col] == objetivo:
            return True #* target is found
        elif matriz[row][col] < objetivo:
            left = k + 1
        else:
            right = k - 1

    return False #* target is not found


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # true
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # false
