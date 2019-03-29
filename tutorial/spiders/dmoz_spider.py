import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["cnn.com"]
    start_urls = [
        "https://edition.cnn.com/",
    ]
    
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename,'wb') as f:
            f.write(response.body)  