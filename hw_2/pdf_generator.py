import os
import uuid
import subprocess
from datetime import datetime

import table_generator

from image_generator_alkosenko import image_generator

BASE_DIR = "/tmp"


def __compile_tex_file(file_path):
    subprocess.call(["pdflatex", f"-output-directory={BASE_DIR}", file_path], stdout=subprocess.PIPE)


def generate_pdf_file(table: list[list]):
    """
    Generates pdf file with table and random image. 
    """

    filename = "my_generated_pdf_file"
    file_path = os.path.join(BASE_DIR, f"{filename}")

    with open(file_path, "w", encoding="utf-8") as tex:
        tex.write(
            f"\\documentclass{{article}}\n"
            f"\\usepackage{{graphicx}}\n"
            f"\\title{{}}\n"
            f"\\author{{}}\n"
            f"\\date{{{datetime.now().strftime('%d-%m-%y')}}}\n"
            f"\\begin{{document}}\n"
            f"\\maketitle\n"
        )

        image_generator.generate_image(f"{file_path}.jpg")
        tex_table = table_generator.generate_table(table)
        
        tex.write(f"\\includegraphics{{{file_path}.jpg}}\n")
        tex.write(tex_table)
        tex.write("\\end{document}")

    __compile_tex_file(file_path)

    os.remove(file_path)
    os.remove(f"{file_path}.log")
    os.remove(f"{file_path}.aux")
    os.remove(f"{file_path}.jpg")


if __name__ == "__main__":
    table = [[1, 2, 3], ["a", "b", "c"], [1.1, 1.2, 1.3]]

    generate_pdf_file(table)
