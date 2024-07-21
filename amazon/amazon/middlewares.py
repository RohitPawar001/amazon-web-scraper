# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class AmazonSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class AmazonDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

import requests
from random import randint
from urllib.parse import urlencode

class FakeUserAgents:
    
    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings)
    
    def __init__(self,settings):
        self.api_key = settings.get("SCRAPEOPS_API_KEY")
        self.endpoint = settings.get("USER_ENDPOINT","SCRAPEOPS_USER_AGENTS_URL")
        self.user_agents_active = settings.get("USER_AGENTS_ENABLED",False)
        self.num_results = settings.get("NUM_RESULTS")
        self.headers_list = []
        self._get_user_agents_list()
        self._user_agents_enabled()
        
    def _get_user_agents_list(self):
        payload = {"api_key": self.api_key}
        if self.num_results is not None:
            payload["num_results"] = self.num_results
        response = requests.get(self.endpoint,urlencode(payload))
        json_response = response.json()
        self.agents_list = json_response.get("result",[])
        
    def _get_random_agent(self):
        random_index = randint(0,len(self.agents_list)-1)
        return self.agents_list[random_index]
    
    def _user_agents_enabled(self):
        if self.api_key is None or self.api_key == "" or self.user_agents_active == False:
            self.user_agents_active = False
        else:
            self.user_agents_active = True
    
    def process_request(self, request, spider):
        
        random_header = self._get_random_agent()
        request.headers["User-Agent"] = random_header
        
        print("***********HEADER ATTACHED********")
        print(request.headers["User-Agent"])
        
        
class FakeBrowserHeader:
    
    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings)
    
    def __init__(self,settings):
        self.api_key = settings.get("SCRAPEOPS_API_KEY")
        self.header_endpoint = settings.get("BROWSER_ENDPOINT","SCRAPEOPS_BROWSER_HEADER_URL")
        self.browser_header_active = settings.get("BROWSER_HEADER_ENABLED",True)
        self.num_results = settings.get("NUM_RESULTS")
        self.headers_list = []
        self._get_browser_header_list()
        self._browser_header_enabled()
        
    def _get_browser_header_list(self):
        payload = {"api_key": self.api_key}
        if self.num_results is not None:
            payload["num_results"] = self.num_results
        response = requests.get(self.header_endpoint,urlencode(payload))
        json_response = response.json()
        self.headers_list = json_response.get("result",[])
        
    def _get_random_browser_header(self):
        random_index = randint(0,len(self.headers_list)-1)
        return self.headers_list[random_index]
    
    def _browser_header_enabled(self):
        if self.api_key is None or self.api_key == "" or self.browser_header_active == False:
            self.browser_header_active = False
        else:
            self.browser_header_active = True
    
    def process_request(self, request, spider):
        
        random_header = self._get_random_browser_header()
        
        request.headers["accept-language"] = random_header["accept-language"]
        request.headers["sec-ch-ua"] = random_header["sec-ch-ua"]
        request.headers["sec-ch-ua-mobile"] = random_header["sec-ch-ua-mobile"]
        request.headers["sec-ch-ua-platform"] = random_header["sec-ch-ua-platform"]
        request.headers["sec-fetch-site"] = random_header["sec-fetch-site"]
        request.headers["sec-fetch-user"] = random_header["sec-fetch-user"]
        request.headers["sec-fetch-mod"] = random_header["sec-fetch-mod"]
        request.headers["user-agent"] = random_header["user-agent"]
        request.headers["accept"] = random_header["accept"]
        request.headers["upgrade-insecure-requests"] = random_header.get("upgrade-insecure-requests")
        
        print("***************HEADERS ATTACHED*******************************************************************************")
        print(request.headers)