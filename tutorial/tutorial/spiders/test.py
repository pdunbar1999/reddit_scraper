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
            yield {
                'title' : title.css('a::text\n').extract(),
                'url' : title.css('a::attr(href)\n')[0].extract(),
                'pageNumber' : pageNumber,
                }
            
        next_page = response.css('span.next-button a::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)
            
            
"""    def link_check(x, y):
    link = y.css('a::attr(href)\n')[1].extract() #link
    if x == '/domain/i.redd.it/': #if the check equals a link to reddit
        reddit_link = response.urljoin(link) #join urls
        return reddit_link #return it
    else:
        return link #return just the normal link, leads to somewhere else          
"""
