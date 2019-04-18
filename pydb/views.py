import pymysql
import json
from django.http import HttpResponse
from redis import StrictRedis


from pydb.student import Bole
from django.shortcuts import render
def mysql(request):
   #pydb = pymysql.connect("172.17.0.2", "root", "root", "onedb")
   pydb = pymysql.connect("localhost", "root", "123", "onedb")
   cu = pydb.cursor()

   #id = request.GET["id"]

   #sql = "select id, title, type, time, url from bole where id = %s" % (id)
   sql = "select id, title, type, time, url from bole"
   cu.execute(sql)
   re = cu.fetchall()
   bs = []

   for k in re:
      b = Bole()
      b.id = k[0]
      b.title = k[1]
      b.type = k[2]
      b.time = k[3]
      b.url = k[4]
      bs.append(b)

   return render(request, "one.html", {"bole":bs})
   #return HttpResponse(json.dumps(re), content_type="application/json")


# def redis(request):
#    redis = StrictRedis(host="172.17.0.3", port=6379, db=0, decode_responses=True)
#
#    list1 = redis.get("name")+" "+redis.get("id")
#
#    return HttpResponse(list1)
#
#
def demo(request):
   return render(request, "two.html")
