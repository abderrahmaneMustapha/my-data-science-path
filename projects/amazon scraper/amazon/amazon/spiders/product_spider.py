import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"

    def start_requests(self):
        urls = [
            'https://www.amazon.com/b?node=17938598011&pf_rd_r=W8409C2R445HHWYXHT7A&pf_rd_p=e5b0c85f-569c-4c90-a58f-0c0a260e45a0',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'text-%s.html' % page
        with open(filename, 'wb') as f:
            for r in  response.css(u"div li.s-result-item a.s-access-detail-page h2").getall():
                f.write(r.encode())
        self.log('Saved file %s' % filename)