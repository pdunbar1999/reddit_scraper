import scrapy

class MySpider(scrapy.Spider):
    name = 'reddit_scrape'
    allowed_domains = ['reddit.com']
    start_urls = [
        'https://www.reddit.com/'
    ]
    

    def parse(self, response):
        for title in response.css('p.title'):               
            yield {
                'title' : title.css('a::text\n').extract(),
                'url' : title.css('a::attr(href)\n').extract(), 
                }
            
        next_page = response.css('span.next-button a::attr(href)').extract_first()
        yield {
            'pageNumber' : 1
            }
        yield response.follow(next_page, callback=self.parse)
            
           
