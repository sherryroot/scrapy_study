# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import numpy as np
import pandas as pd


class read_wbs(object):
    df = pd.read_csv("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/scrapy/scrapy_BOT_ANJVKE/spiders/ajk/ajk/r.csv")

    for i in df['wbs']:
        print(type(i))
        print(i)
