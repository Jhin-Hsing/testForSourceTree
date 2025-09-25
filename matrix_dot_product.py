"""矩陣點積（Frobenius inner product）示範。"""
from __future__ import annotations

from typing import List, Tuple

Matrix = List[List[float]]


def shape(matrix: Matrix) -> Tuple[int, int]:
    """確認矩陣為長方形並回傳 (列數, 欄數)。"""
    if not matrix or not matrix[0]:
        raise ValueError("矩陣至少要有一列與一欄")
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise ValueError("矩陣每一列的欄數必須相同")
    return len(matrix), row_length


def transpose(matrix: Matrix) -> Matrix:
    """回傳矩陣的轉置。"""
    rows, cols = shape(matrix)
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    """計算矩陣乘積 A * B（A 的欄數需等於 B 的列數）。"""
    rows_a, cols_a = shape(a)
    rows_b, cols_b = shape(b)
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


def frobenius_inner_product(a: Matrix, b: Matrix) -> float:
    """計算兩個相同維度矩陣的 Frobenius 內積。"""
    rows, cols = shape(a)
    if shape(b) != (rows, cols):
        raise ValueError("兩個矩陣必須具有相同的形狀才能進行點積")
    return sum(a[r][c] * b[r][c] for r in range(rows) for c in range(cols))


def trace(matrix: Matrix) -> float:
    """回傳方陣的 trace（對角線元素總和）。"""
    rows, cols = shape(matrix)
    if rows != cols:
        raise ValueError("只有方陣才有 trace")
    return sum(matrix[i][i] for i in range(rows))


def trace_of_product(a: Matrix, b: Matrix) -> float:
    """利用 trace(A^T * B) 證明 Frobenius 內積的等價性。"""
    rows, cols = shape(a)
    if shape(b) != (rows, cols):
        raise ValueError("A 與 B 必須同維度")
    product = multiply(transpose(a), b)
    return trace(product)


def pretty_print(name: str, matrix: Matrix) -> None:
    """輸出矩陣名稱與內容以便閱讀。"""
    rows, cols = shape(matrix)
    print(f"{name} ({rows}x{cols}):")
    for row in matrix:
        print("  ", "  ".join(f"{value:7.3f}" for value in row))
    print()


def main() -> None:
    """展示矩陣間 Frobenius 點積的計算與性質。"""
    a: Matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    b: Matrix = [
        [7, 8, 9],
        [1, 0, -1],
    ]

    pretty_print("矩陣 A", a)
    pretty_print("矩陣 B", b)

    inner = frobenius_inner_product(a, b)
    print("Frobenius 內積 =", inner)
    print("逐項計算：", " + ".join(
        f"{a[r][c]}*{b[r][c]}" for r in range(len(a)) for c in range(len(a[0]))
    ))
    print()

    transposed = transpose(a)
    product = multiply(transposed, b)
    pretty_print("A^T * B", product)

    trace_value = trace(product)
    print("trace(A^T * B) =", trace_value)
    print("與 Frobenius 內積相同，代表兩種定義一致。")


if __name__ == "__main__":
    main()
