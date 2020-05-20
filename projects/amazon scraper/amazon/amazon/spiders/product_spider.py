import scrapy


class QuotesSpider(scrapy.Spider):
    name = "amazon-main"

    def start_requests(self):
        urls = [
            'https://www.amazon.com/?ref=icp_country_in_t1',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'text-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)