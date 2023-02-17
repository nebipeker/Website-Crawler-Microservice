import unittest
import grpc
import time
import subprocess


class TestDocker(unittest.TestCase):
    def setUp(self):
        # Start the Docker container
        self.container_id = subprocess.check_output(["docker", "run", "-d", "-p", "50051:50051", "website-crawler"]).decode().strip()

        # Wait for the server to start up
        self.channel = grpc.insecure_channel("localhost:50051")
        for _ in range(10):
            try:
                grpc.channel_ready_future(self.channel).result(timeout=1)
                break
            except:
                time.sleep(1)

    def tearDown(self):
        # Stop the Docker container
        subprocess.run(["docker", "stop", self.container_id])

    def test_crawl_website(self):
        # Test crawling a website using the microservice
        from website_crawler_pb2 import WebsiteCrawlerRequest
        from website_crawler_pb2_grpc import WebsiteCrawlerStub

        website_url = "https://www.example.com"
        expected_urls = {
            "https://www.example.com/",
            "https://www.example.com/page1",
            "https://www.example.com/page2",
        }

        stub = WebsiteCrawlerStub(self.channel)
        request = WebsiteCrawlerRequest(website_url=website_url)
        response = stub.CrawlWebsite(request)

        self.assertSetEqual(set(response.urls), expected_urls)


if __name__ == '__main__':
    unittest.main()
