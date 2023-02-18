import grpc

# import the generated classes
import website_crawler_pb2
import website_crawler_pb2_grpc

def run():
    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:50051')

    # create a stub (client)
    stub = website_crawler_pb2_grpc.WebsiteCrawlerServiceStub(channel)

    # create a request message
    request = website_crawler_pb2.WebsiteCrawlerRequest(website_url='http://example.com')

    # make the gRPC call
    response = stub.CrawlWebsite(request)

    # print the response
    print(response)

if __name__ == '__main__':
    run()
