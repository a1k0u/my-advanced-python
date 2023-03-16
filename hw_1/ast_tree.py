#!/home/alkosenko/miniconda3/bin/python

import sys
import os
import collections
import ast
import networkx
import astunparse
import inspect
from networkx.drawing.nx_pydot import write_dot
from typing import TypeVar
from typing import Union
import networkx as nx
import matplotlib.pyplot as plt

T = TypeVar("T")


def __rename_object(e: T) -> Union[T, str]:
    names = {
        ast.Add: "+",
        ast.Lt: "<",
        ast.BinOp: "binOp",
        ast.Subscript: "getList",
        ast.If: "if",
        ast.For: "for",
        ast.Return: "ret",
        ast.Compare: "cmpr",
        ast.FunctionDef: "func",
        ast.Tuple: "()",
        ast.List: "[]",
        ast.Constant: "const",
        ast.Name: "var",
        ast.arguments: "args",
        ast.arg: "arg",
    }

    for name in names:
        if isinstance(e, name):
            return names[name]
    return e


def foo(e):
    if isinstance(e, (ast.Store, ast.Load, ast.ImportFrom)):
        return None

    if isinstance(e, (int, float, str)):
        return str(e)

    name = __rename_object(e)
    root = {name: []}

    _dirs = [e_ for e_ in dir(e) if not e_.startswith("_")]

    for method in _dirs:
        if method in [
            "col_offset",
            "end_col_offset",
            "end_lineno",
            "lineno",
            "n",
            "s",
            "kind",
        ]:
            continue

        _get_attr = getattr(e, method)

        if isinstance(_get_attr, list):
            root[name].extend([node for attr in _get_attr if (node := foo(attr))])
        else:
            root[name].append(node) if (node := foo(_get_attr)) else None

    return root


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("Two arguments are required..")

    _, filename = sys.argv

    if not os.path.exists(filename):
        exit("File does not exist..")

    file = open(filename, "r", encoding="utf-8")

    file_read = file.read()

    # print(astunparse.dump(ast.parse(file_read)))
    import json
    # print(json.loads(ast.dump(ast.parse(file_read), indent=4)))
    # root = Tree("")
    # G = nx.DiGraph()

    # def bar(root: Tree):
    #     q = collections.deque()
    #     q.appendleft(root)

    #     while q:
    #         n: Tree = q.popleft()
    #         print(n.name)
    #         G.add_node(str(n.name))

    #         for child in n.children:
    #             # print(child)
    #             # print(q)
    #             G.add_node("Child_%s" % child.name)
    #             G.add_edge(n.name, "Child_%s" % child.name)

    #             q.extend(child.children)
    #             # print(q)

    # root.children.append(foo(ast.parse(file_read)))
    # print(root.children[0].children[0].children)
    # bar(root)
    # nx.draw(G)
    # plt.show()


    # nx.write_dot(G,'test.dot')

    # # same layout using matplotlib with no labels
    # plt.title('draw_networkx')
    # pos=nx.graphviz_layout(G, prog='dot')
    # nx.draw(G, pos, with_labels=False, arrows=False)
    # plt.savefig('nx_test.png')
    print(astunparse.dump(ast.parse(file_read)))
    # print(dir(ast.parse(file_read).body[1].body[0].targets[0].elts[0]))
    # print(ast.parse(file_read).body[1].body[0].targets[0].elts[0].id)
    # for i in ast.walk(ast.parse(file_read)):
    #     print(ast.dump(i), "\n -- \n")
