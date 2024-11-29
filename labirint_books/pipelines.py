# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class LabirintBooksPipeline:

    # Отерытие файла для записи 
    def open_spider(self, spider):
        self.file = open('labirint_books.json', 'a', encoding="utf-8")

    # Закрытие файла
    def close_spider(self, spider):
        self.file.close()

    # Обработка данных и запись в файл JSON
    def process_item(self, item, spider):
        try:
            if not item.get("id"):
                item["id"] = 000
            else:
                item["id"] = int(item.get("id").split(":")[1].strip())
        except:
            item["id"] = 000

        try:
            if not item['isbn']:
                item['isbn'] = 000
            else:
                item['isbn'] = item.get("isbn").split(":")[1].strip()
        except:
            item['isbn'] = 000

        try:
            if not item.get("title"):
                item["title"] = "no_title"
            else:    
                title = item.get("title").split(":")
                if len(title) <= 1:
                    item["title"] = title
                else:
                    item["title"] = title[1].strip()
        except:
            item["title"] = "no_title"

        try:
            if not item.get("author"):
                item["author"] = "no_author"
            else:
                item["author"] = item.get("author")
        except:
            item["author"] = "no_author"

        try:
            if not item.get("rate"):
                item["rate"] = 0.0
            else:   
                item["rate"] = float(item.get("rate"))
        except:
            item["rate"] = 0.0

        book = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + "\n"
        self.file.writelines(book)
        
        return item
        
