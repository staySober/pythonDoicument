#!/usr/bin/env python
#coding=utf-8

#爬去商祥
import pymysql
import urllib
import requests
import re
import json  
import codecs
# 打开数据库连接
db = pymysql.connect("rr-bp1x8k8pea67a270co.mysql.rds.aliyuncs.com","yit_prod_r","n3bh14ctpmb4","yit_prod_magento" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用execute查询
sql = "SELECT spu.id, media.url \
FROM yitiao_product_spu spu \
  LEFT JOIN yitiao_media media ON spu.product_desc_id = media.id \
  LEFT JOIN yitiao_product_sku sku ON sku.spu_id = spu.id \
  LEFT JOIN yitiao_product_sku_stock stock ON stock.sku_id = sku.id \
  LEFT JOIN yitiao_product_on_sale spu_on_sale ON spu_on_sale.product_id = spu.id \
  LEFT JOIN yitiao_product_on_sale sku_on_sale ON sku_on_sale.product_id = sku.id \
WHERE spu.visibility = 2 AND spu_on_sale.on_sale = 1 AND sku_on_sale.on_sale = 1"

# 字典存储key value
descStorage = {}

try :
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results :
            mediaUrl = row[1]
            spuId = row[0]
            # add    
            descStorage[spuId] = mediaUrl
            # print
            print("spuId : %s  url: %s" % \
                (spuId, mediaUrl))

except :
    print("ERROR : unable to fetch data")

db.close()

# 字典储存真正的商祥文本

descRealStorage = {}

tup = descStorage.items()
for spuId,url in tup :
    stream = requests.get(url, stream=True)
    desctemp = stream.content.decode("UTF-8",'strict')
    # 去html标签
    dr = re.compile(r'<[^>]+>',re.S)
    desctemp = dr.sub('',desctemp)
    desctemp = desctemp.replace("&nbsp;","")
    desctemp = desctemp.replace("&","")
    # add
    descRealStorage[spuId] = desctemp
    # log
    print("spuId : %s fetch success", spuId)

# save
file = codecs.open("/Users/sober/Desktop/spuDesccrawler.txt","w+",encoding= "UTF-8")
data = json.dumps(descRealStorage,ensure_ascii=False)
file.write(data)
file.close()


