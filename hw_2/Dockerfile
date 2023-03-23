FROM python:3.9
WORKDIR /the/workdir/path
COPY . .
RUN apt-get update && \
    apt-get install -y texlive-latex-base
RUN pip install numpy
RUN pip install Pillow
RUN pip install image-generator-alkosenko
ENTRYPOINT ["python3", "/the/workdir/path/pdf_generator.py"]
