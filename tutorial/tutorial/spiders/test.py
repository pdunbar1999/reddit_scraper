import scrapy

class MySpider(scrapy.Spider):
    name = 'reddit_scrape'
    allowed_domains = ['reddit.com']
    start_urls = [
        'https://www.reddit.com/'
    ]
    
    global pageNumber
    pageNumber = 0

    def parse(self, response):
        global pageNumber
        pageNumber = pageNumber + 1
        for title in response.css('p.title'):
            check = response.css('span.domain a::attr(href)')[0].extract()
            link = title.css('a::attr(href)')[0].extract() #link
            if check == '/domain/i.redd.it/': #if the check equals a link to reddit
                link = response.urljoin(link) #join urls
                
            yield {
                'title' : title.css('a::text\n\n')[0].extract(),
                'url' : link,
                'pageNumber' : pageNumber,
                }
            
        next_page = response.css('span.next-button a::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)
            
