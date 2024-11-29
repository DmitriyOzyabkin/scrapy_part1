# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class LabirintBooksPipeline:

    def open_spider(self, spider):
        self.file = open('labirint_books.json', 'a', encoding="utf-8")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):

        item["id"] = int(item.get("id").split(":")[1].strip())
        item['isbn'] = item.get("isbn").split(":")[1].strip()
        title = item.get("title")
        if len(title) <= 1:
            item["title"] = title
            # json.encoder(item["title"])
        else:
            item["title"] = title.split(":")[1].strip()
        item["rate"] = float(item.get("rate"))

        book = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + "\n"
        self.file.writelines(book)
        print()
        return item
        
