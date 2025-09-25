"""單位矩陣示範與相關性質說明。"""
from __future__ import annotations

from typing import List

Matrix = List[List[float]]


def identity_matrix(size: int) -> Matrix:
    """生成 size x size 的單位矩陣 (I_size)。"""
    if size <= 0:
        raise ValueError("單位矩陣的階數必須是正整數")
    return [[1.0 if r == c else 0.0 for c in range(size)] for r in range(size)]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    """回傳矩陣乘積 A * B（A 的欄數需等於 B 的列數）。"""
    rows_a = len(a)
    cols_a = len(a[0]) if a else 0
    rows_b = len(b)
    cols_b = len(b[0]) if b else 0
    if rows_a == 0 or cols_a == 0 or rows_b == 0 or cols_b == 0:
        raise ValueError("矩陣不得為空")
    if cols_a != rows_b:
        raise ValueError("A 的欄數必須等於 B 的列數")
    result: Matrix = []
    for r in range(rows_a):
        row: List[float] = []
        for c in range(cols_b):
            cell = sum(a[r][k] * b[k][c] for k in range(cols_a))
            row.append(cell)
        result.append(row)
    return result


def pretty_print(name: str, matrix: Matrix) -> None:
    """輸出矩陣名稱與內容以便閱讀。"""
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    print(f"{name} ({rows}x{cols}):")
    for row in matrix:
        print("  ", "  ".join(f"{value:5.1f}" for value in row))
    print()


def main() -> None:
    """展示單位矩陣在矩陣乘法中的身分元素特性。"""
    a: Matrix = [
        [2, -1],
        [0, 3],
    ]
    identity = identity_matrix(2)

    left = multiply(identity, a)
    right = multiply(a, identity)

    pretty_print("單位矩陣 I", identity)
    pretty_print("矩陣 A", a)
    pretty_print("I * A", left)
    pretty_print("A * I", right)
    print("當 I 為單位矩陣時，I * A 與 A * I 都會還原 A。")


if __name__ == "__main__":
    main()
