"""簡易矩陣運算示範，無使用者互動。"""
from __future__ import annotations

from typing import List, Tuple

Matrix = List[List[float]]


def shape(matrix: Matrix) -> Tuple[int, int]:
    """確認矩陣為長方形並回傳 (列數, 欄數)。"""
    if not matrix or not matrix[0]:
        raise ValueError("Matrix must have at least one row and one column")
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise ValueError("Matrix rows must have the same length")
    return len(matrix), row_length


def add(a: Matrix, b: Matrix) -> Matrix:
    """在兩個相同維度的矩陣上做元素加總。"""
    rows, cols = shape(a)
    if shape(b) != (rows, cols):
        raise ValueError("Matrices must have the same shape to be added")
    return [[a[r][c] + b[r][c] for c in range(cols)] for r in range(rows)]


def subtract(a: Matrix, b: Matrix) -> Matrix:
    """在兩個相同維度的矩陣上做元素相減。"""
    rows, cols = shape(a)
    if shape(b) != (rows, cols):
        raise ValueError("Matrices must have the same shape to be subtracted")
    return [[a[r][c] - b[r][c] for c in range(cols)] for r in range(rows)]


def scalar_multiply(scalar: float, matrix: Matrix) -> Matrix:
    """將矩陣中的每個元素都乘上同一個純量。"""
    rows, cols = shape(matrix)
    return [[scalar * matrix[r][c] for c in range(cols)] for r in range(rows)]


def transpose(matrix: Matrix) -> Matrix:
    """交換矩陣的列與欄 (m x n -> n x m)。"""
    rows, cols = shape(matrix)
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    """計算 A * B 的矩陣乘法，確保內部維度相符。"""
    rows_a, cols_a = shape(a)
    rows_b, cols_b = shape(b)
    if cols_a != rows_b:
        raise ValueError("Number of columns of A must equal number of rows of B")
    result: Matrix = []
    for r in range(rows_a):
        row: List[float] = []
        for c in range(cols_b):
            cell = sum(a[r][k] * b[k][c] for k in range(cols_a))
            row.append(cell)
        result.append(row)
    return result


def print_matrix(name: str, matrix: Matrix) -> None:
    """輸出矩陣名稱、維度與格式化數值。"""
    rows, _ = shape(matrix)
    print(f"{name} ({rows}x{len(matrix[0])}):")
    for row in matrix:
        formatted = "  ".join(f"{value:8.3f}" for value in row)
        print(f"    {formatted}")
    print()


def main() -> None:
    """以固定資料展示基礎矩陣運算。"""
    a: Matrix = [
        [2, 3, 1],
        [0, -1, 4],
    ]
    b: Matrix = [
        [5, -2, 0],
        [3, 1, 7],
    ]
    c: Matrix = [
        [1, 0],
        [2, -1],
        [3, 4],
    ]

    print_matrix("Matrix A", a)
    print_matrix("Matrix B", b)
    print_matrix("Matrix C", c)

    print_matrix("A + B", add(a, b))
    print_matrix("A - B", subtract(a, b))
    print_matrix("2 * A", scalar_multiply(2, a))
    print_matrix("transpose(A)", transpose(a))

    product = multiply(a, transpose(b))
    print_matrix("A * transpose(B)", product)

    composed = multiply(a, c)
    print_matrix("A * C", composed)


if __name__ == "__main__":
    main()
