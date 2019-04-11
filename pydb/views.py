import pymysql
import json
from django.http import HttpResponse
from redis import StrictRedis

def mysql(request):
   pydb = pymysql.connect("172.17.0.2", "root", "root", "onedb")
   cu = pydb.cursor()
   cu.execute("select id, name, score from student")
   re = cu.fetchall()
   return HttpResponse(json.dumps(re), content_type="application/json")

def redis(request):
   redis = StrictRedis(host="172.17.0.3", port=6379, db=0, decode_responses=True)

   list1 = redis.get("name")+" "+redis.get("id")

   return HttpResponse(list1)

def demo(request):
   return HttpResponse("测试数据")
