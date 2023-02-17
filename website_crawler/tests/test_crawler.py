import unittest
import website_crawler


class TestWebsiteCrawler(unittest.TestCase):
    def test_crawl_website(self):
        # Test crawling a simple website with two pages
        website_url = "https://www.example.com"
        expected_urls = {
            "https://www.example.com/",
            "https://www.example.com/page1",
            "https://www.example.com/page2",
        }
        crawler = website_crawler.WebsiteCrawler()
        urls = crawler.crawl_website(website_url)
        self.assertSetEqual(set(urls), expected_urls)

    def test_crawl_website_invalid_url(self):
        # Test crawling an invalid website URL
        website_url = "not_a_website_url"
        crawler = website_crawler.WebsiteCrawler()
        with self.assertRaises(Exception):
            urls = crawler.crawl_website(website_url)


if __name__ == '__main__':
    unittest.main()
