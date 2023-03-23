FROM python:3.9

WORKDIR /the/workdir/path
COPY . .

RUN apt-get update
RUN apt-get install -y texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install numpy
RUN python3 -m pip install Pillow
RUN python3 -m pip install image-generator-alkosenko
CMD [ "python3", "pdf_generator.py" ]