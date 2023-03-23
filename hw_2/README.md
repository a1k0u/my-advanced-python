docker build . -t pdf

e=`docker run --rm -d pdf}` && docker cp $e:/my_generated_pdf_file.pdf . && docker stop $e