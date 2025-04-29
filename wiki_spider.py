import scrapy
from urllib.parse import urlparse
import os

class WikiSpider(scrapy.Spider):
    name = "wiki"


    custom_settings = {
        'FEEDS': None
    }

    start_urls = [
        'https://wiki.deepin.org/zh/home',
        'https://wiki.deepin.org/zh/开发者/开发指南',
        #此处加入剩余网址
    ]

    def parse(self, response):
        # 提取页面标题
        title = response.css('title::text').get()
        if title:
            title = title.strip()
        else:
            title = 'untitled'

        content_div = response.css('template[slot="contents"] div').get()
        if not content_div:
            self.logger.warning(f'页面 {response.url} 没有找到正文内容')
            return

        # 清理HTML标签，保留纯文本
        content_text = response.css('template[slot="contents"] div *::text').getall()
        content_text = '\n'.join(line.strip() for line in content_text if line.strip())

        # 生成Markdown内容
        markdown_content = f"# {title}\n\n{content_text}"

        # 生成文件名
        parsed_url = urlparse(response.url)
        path = parsed_url.path.strip('/').replace('/', '_') or 'index'
        filename = f"{path}.md"

        # 保存路径
        save_dir = 'deepin_wiki'
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, filename)

        # 写入Markdown文件
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        self.logger.info(f"已保存: {save_path}")
