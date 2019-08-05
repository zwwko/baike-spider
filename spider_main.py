import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloder = html_downloader.HtmlDownloader()
        self.outpuer = html_outputer.HtmlOutputer()
        self.parser = html_parser.HtmlParser()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print ('craw %d : %s' % (count, new_url))
                html_cont = self.downloder.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outpuer.collect_data(new_data)

                if count==100:
                    break
                count = count + 1
            except:
                print ('craw failed')


        self.outpuer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
