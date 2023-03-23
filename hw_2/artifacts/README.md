PyPi -> [https://pypi.org/project/image-generator-alkosenko/](https://pypi.org/project/image-generator-alkosenko/)


```shell
docker build . -t pdf_alkosenko
```

```shell
e=`docker run --rm -d pdf` && docker cp $e:/tmp/my_generated_pdf_file.pdf . && docker stop $e
```