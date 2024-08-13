from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider

class FlexibleSpider(CrawlSpider):
    name = "flexiblecrawler"

    # Modify these attributes as per your requirement
    allowed_domains = ["example.com"]
    start_urls = ["http://example.com/"]
    rules = (
        Rule(LinkExtractor(allow=r'items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        """
        This method should be modified by the user to define how the scraped data is processed.
        """

        # Example of data extraction logic that you should modify as needed
        item = {
            'title': response.xpath('//h1/text()').get(),
            'price': response.xpath('//p[@class="price_color"]/text()').get(),
            'availability': response.xpath('//p[@class="instock availability"]/text()').get(),
        }

        # Example to show the output, this should be tailored to the site's structure
        if not item['title']:
            raise CloseSpider('No items found')

        yield item
