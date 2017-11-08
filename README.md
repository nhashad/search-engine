<h2 align="center">Search Engine</h2>

1. Install scrapy from : https://scrapy.org/
2. Install newspaper3k from: http://newspaper.readthedocs.io/en/latest/user_guide/install.html#install & `pip install newspaper3k`


### To run :

1. open a conda prompt: `conda create --name py36 python=3.6`
2. `source activate py36`
3. `cd ~/search-engine/src/newyorktimes/newyorktimes`
4. `scrapy crawl newyorktimescrawler -o test.csv`
