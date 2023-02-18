import grpc
import website_crawler_pb2
import website_crawler_pb2_grpc
import requests
from bs4 import BeautifulSoup


class WebsiteCrawlerServicer(website_crawler_pb2_grpc.WebsiteCrawlerServiceServicer):
    def CrawlWebsite(self, request, context):
        try:
            page = requests.get(request.website_url)
            soup = BeautifulSoup(page.content, 'html.parser')
            urls = []
            for link in soup.find_all('a'):
                href = link.get('href')
                if href and href.startswith('http'):
                    urls.append(href)
            return website_crawler_pb2.WebsiteCrawlerResponse(urls=urls)
        except:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('Error occurred while crawling website')
            return website_crawler_pb2.WebsiteCrawlerResponse()


def serve():
    server = grpc.server(grpc.ThreadPoolExecutor(max_workers=10))
    website_crawler_pb2_grpc.add_WebsiteCrawlerServiceServicer_to_server(
        WebsiteCrawlerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
