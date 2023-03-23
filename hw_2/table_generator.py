from functools import reduce


def __concat_values_with_sep(x: any, y: any, symbol: str):
    return f"{x}{symbol}{y}"


def __create_table_rows(values: list[list]):
    return reduce(
        lambda x, y: __concat_values_with_sep(x, y, " \\\\\n"),
        map(
            lambda l: reduce(lambda x, y: __concat_values_with_sep(x, y, " & "), l),
            values,
        ),
    )


def generate_table(values: list[list]):
    """
    Latex table generator in functional programming style.
    """

    return (
        "\\begin{table}[htbp]\n\\begin{tabular}{lllll}"
        + f"\n{__create_table_rows(values)}\n"
        + "\\end{tabular}\n\\end{table}\n"
    )


if __name__ == "__main__":
    print(generate_table([[1, 2, 3], ["a", "b", "c"], [1.1, 1.2, 1.3]]))