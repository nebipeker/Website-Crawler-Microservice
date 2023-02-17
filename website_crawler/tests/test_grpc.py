import unittest
import grpc
import concurrent.futures
import time
import threading

import website_crawler_pb2
import website_crawler_pb2_grpc
import website_crawler


class TestGRPC(unittest.TestCase):
    def setUp(self):
        # Start the gRPC server
        server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
        website_crawler_pb2_grpc.add_WebsiteCrawlerServicer_to_server(WebsiteCrawlerServicer(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        self.server = server

        # Start the gRPC client
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = website_crawler_pb2_grpc.WebsiteCrawlerStub(self.channel)

    def tearDown(self):
        # Stop the gRPC server
        self.server.stop(None)

    def test_crawl_website(self):
        # Test crawling a website using gRPC
        website_url = "https://www.example.com"
        expected_urls = {
            "https://www.example.com/",
            "https://www.example.com/page1",
            "https://www.example.com/page2",
        }
        request = website_crawler_pb2.WebsiteCrawlerRequest(website_url=website_url)
        response = self.stub.CrawlWebsite(request)
        self.assertSetEqual(set(response.urls), expected_urls)


class WebsiteCrawlerServicer(website_crawler_pb2_grpc.WebsiteCrawlerServicer):
    def CrawlWebsite(self, request, context):
        # Crawl the website and return the results
        crawler = website_crawler.WebsiteCrawler()
        urls = crawler.crawl_website(request.website_url)
        response = website_crawler_pb2.WebsiteCrawlerResponse(urls=urls)
        return response


if __name__ == '__main__':
    unittest.main()
