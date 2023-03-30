import numpy as np


class StrMixin:
    def __str__(self):
        return "\n".join(str(row) for row in self.matrix)


class WriteToFileMixin:
    def write_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(str(self))


class SetterGetterMixin:
    def __get__(self):
        return self.matrix

    def __set__(self, matrix):
        self.matrix = matrix


class MatrixMixin(
    np.lib.mixins.NDArrayOperatorsMixin, SetterGetterMixin, WriteToFileMixin, StrMixin
):
    def __init__(self, matrix):
        self.matrix = np.asarray(matrix)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get("out", None)

        inputs = tuple(x.matrix if isinstance(x, MatrixMixin) else x for x in inputs)

        return getattr(ufunc, method)(*inputs, out=out, **kwargs)


if __name__ == "__main__":
    import numpy as np

    def write_artifacts(artifact, filename):
        file = open(f"{filename}.txt", "w")
        print(artifact, file=file)
        file.close()

    np.random.seed(0)

    A = MatrixMixin(np.random.randint(0, 10, (10, 10)))
    B = MatrixMixin(np.random.randint(0, 10, (10, 10)))

    write_artifacts(A + B, "artifacts/medium/matrix+")
    write_artifacts(A * B, "artifacts/medium/matrix*")
    write_artifacts(A @ B, "artifacts/medium/matrix@")
