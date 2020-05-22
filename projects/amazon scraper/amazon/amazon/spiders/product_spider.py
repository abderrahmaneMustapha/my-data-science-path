import scrapy
import pandas as pd

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    data_dict = []
    allowed_domains = ['amazon.com']
  
    
    def start_requests(self):
        root_url = [
            'https://www.amazon.com/b?node=17938598011&pf_rd_r=W8409C2R445HHWYXHT7A&pf_rd_p=e5b0c85f-569c-4c90-a58f-0c0a260e45a0',
        ]
    

        for urls in root_url:
            yield scrapy.Request(url=urls, callback=self.parse)
        for f in open("urls.txt", "r").readlines():
            yield scrapy.Request(url=f, callback=self.get_data)
        
      
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'urls.txt'
        with open(filename, 'wb') as f:
            for r in  response.css(u"div li.s-result-item a.s-access-detail-page::attr(href)").getall():
                f.write(r.encode())
                f.write("\n".encode())
        self.log('Saved file %s' % filename)
        
    def get_data(self, response):
        # get name
        name= response.url.split("/")[3].replace("-", " ")

        # get the brand 
        href = response.xpath('//a[@id="bylineInfo"]/@href').get()
        brand  = href.split("/")[2] if len(href.split("/")[2]) > 2 else href.split("/")[1]

        #get total rate
        total_rate = response.xpath('//span[@id="acrCustomerReviewText"]/text()').get().split(" ")[0]

        #get rate
        rate = response.xpath('//span[@id="acrPopover"]/@title').get().split(" ")[0]

        #get price
        
        price= response.xpath('//span[@id="priceblock_ourprice"]/text()').get()

        #get description
        description= ' '.join(response.xpath('//span[@id="productTitle"]/text()').get().split())
        
        #image link 
        image_link =  response.xpath('//div[@id="ivLargeImage"]//img//@src').get()

        #link
        link = response.url
        
        self.data_dict.append({"name" : name ,  "brand" : brand, "price" : price,
                        "rating" : rate, "total_rating":total_rate, "description": description, 
                        "image_link":image_link, 'link':  link
                         })
                                  
        df = pd.DataFrame(self.data_dict,columns=['name', 'brand','price', 'rating', 'total_ratings', 
                                  'description', 'image_link', 'link'])
        print(self.data_dict)
        df.to_csv('my_csv.csv')
       
       



        