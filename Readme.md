## Requirement

Python3  
pip

## INSTALL

pip install Scrapy==2.0.1  
pip install requests==2.21.0

## RUN  
cd webscrap  
scrapy crawl nlm -a author='author name'  
eg:  
scrapy crawl nlm -a author='Sudarshan S'  

## Output
/tmp/items.json


## Docker run  
docker run -it -e AUTHOR='Sudarshan S' -v /tmp:/data dhayanidhi/exp.hollow.webcrawl:0.3