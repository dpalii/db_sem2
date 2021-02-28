from scrapy import cmdline
import os


def crawl():
    try:
        os.remove("results/odissey.xml")
    except OSError:
        print("results/odissey.xml not found")
    cmdline.execute("scrapy crawl odissey -o results/odissey.xml".split())

crawl()
