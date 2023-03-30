from typing import Iterable
from typing import Callable


class Matrix:
    def __init__(self, matrix: Iterable[Iterable]) -> None:
        assert isinstance(matrix, Iterable)
        assert len(matrix)
        assert all([isinstance(row, Iterable) for row in matrix])
        assert len({len(row) for row in matrix}) == 1

        self.__matrix = matrix
        self.__rows = len(matrix)
        self.__columns = len(matrix[0])

    def get_size(self):
        return self.__rows, self.__columns

    def is_size_equal(self, other) -> bool:
        if not isinstance(other, Matrix):
            raise TypeError

        if self.get_size() != other.get_size():
            return False
        return True

    def is_size_fit_to_matmul(self, other) -> bool:
        if not isinstance(other, Matrix):
            raise TypeError

        if self.__columns != other.__rows:
            return False
        return True

    def __matrix_element_operation(self, other, operation: Callable):
        if not self.is_size_equal(other):
            raise ValueError

        result = [[0 for _ in range(self.__columns)] for _ in range(self.__rows)]
        for i in range(self.__rows):
            for j in range(self.__columns):
                result[i][j] = operation(self.__matrix[i][j], other.__matrix[i][j])
        return Matrix(result)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __add__(self, other):
        return self.__matrix_element_operation(other, lambda x, y: x + y)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __mul__(self, other):
        return self.__matrix_element_operation(other, lambda x, y: x * y)

    def __imatmul__(self, other):
        return self.__matmul__(other)

    def __matmul__(self, other):
        if not self.is_size_fit_to_matmul(other):
            raise ValueError

        result = [[0 for _ in range(other.__columns)] for _ in range(self.__rows)]
        for i in range(self.__rows):
            for j in range(other.__columns):
                result[i][j] = sum(
                    [
                        self.__matrix[i][k] * other.__matrix[k][j]
                        for k in range(self.__columns)
                    ]
                )
        return Matrix(result)

    def __str__(self) -> str:
        return self.__matrix.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self):
        return sum([sum(row) for row in self.__matrix])


if __name__ == "__main__":
    import numpy as np

    def write_artifacts(artifact, filename):
        file = open(f"{filename}.txt", "w")
        print(artifact, file=file)
        file.close()

    np.random.seed(0)

    # Easy

    A = Matrix(np.random.randint(0, 10, (10, 10)))
    B = Matrix(np.random.randint(0, 10, (10, 10)))

    write_artifacts(A + B, "artifacts/easy/matrix+")
    write_artifacts(A * B, "artifacts/easy/matrix*")
    write_artifacts(A @ B, "artifacts/easy/matrix@")

    # Hard

    A = Matrix([[1, 5], [3, 8]])
    B = D = Matrix([[1, 0], [0, 1]])
    C = Matrix([[9, 4], [2, 2]])

    write_artifacts(A @ B, "artifacts/hard/AB.txt")
    write_artifacts(C @ D, "artifacts/hard/CD.txt")
    write_artifacts(f"{hash(A @ B)}\n{hash(C @ D)}", "artifacts/hard/hash.txt")
