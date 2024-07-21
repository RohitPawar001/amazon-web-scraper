import scrapy
from amazon.items import MobileItem

class MobileSpider(scrapy.Spider):
    name = "mobile"
    allowed_domains = ["www.amazon.in"]
    start_urls = ["https://www.amazon.in/s?bbn=1389401031&rh=n%3A1389401031%2Cp_89%3AApple&dc&qid=1717581794&rnid=3837712031&ref=lp_1389401031_nr_p_89_0"]

    def parse(self, response):
        mobiles = response.css(".puis-card-border")
        for mobile in mobiles:
            mobile_url = response.css(".a-text-normal::attr(href)").get()
            mobile_page_url = "https://www.amazon.in" + mobile_url
            
            yield response.follow(mobile_page_url,callback = self.parse_mobile_page)

        next_page = response.css(".s-pagination-separator::attr(href)").get()
        if next_page is not None:
            next_page_url = "https://www.amazon.in" + next_page
            yield response.follow(next_page_url,callback = self.parse)
        
        
    def parse_mobile_page(self,response):
        table = response.css("table.a-normal.a-spacing-micro tr")
        mobile_item = MobileItem()
        
        mobile_item["title"] = response.css("#productTitle::text").get()
        mobile_item["brand"] = table[0].css(".a-size-base.po-break-word::text").get()
        mobile_item["os"] = table[1].css(".a-size-base.po-break-word::text").get()
        mobile_item["memory_size"] = table[2].css(".a-size-base.po-break-word::text").get()
        mobile_item["screen_size"] = table[3].css(".a-size-base.po-break-word::text").get()
        mobile_item["screen_resolution"] = table[4].css(".a-size-base.po-break-word::text").get()
        mobile_item["price"] = response.css(".a-price-whole::text").get()
        mobile_item["discount"] = response.css(".a-size-large.a-color-price.savingPriceOverride.aok-align-center.reinventPriceSavingsPercentageMargin.savingsPercentage::text").get()
        mobile_item["price_without_discount"] = response.css(".a-size-small.aok-offscreen::text").get()
        mobile_item["star_rating"] = response.css(".a-size-base.a-color-base::text").get()
        mobile_item["num_ratings"] = response.css("#acrCustomerReviewText.a-size-base::text").get()
        mobile_item["availibility"] = response.css(".a-size-medium.a-color-success::text").get()
        
        yield mobile_item 