import datetime
from flask import jsonify, request, flash
from sqlalchemy import func
from run import app;
from apps.post.models.post_info import Post
from run import db
from geoalchemy2.comparator import Comparator
import timeago

@app.route("/getPost", methods=["GET"])
def getPost():
    args = request.args
    lon = str(args.get('lon'))
    lat = str(args.get('lat'))
    # if None in (lon, lat):
    #     raise Exception("Invalid")
   
    q = db.session.query(Post.message,Post.location,Post.created_on).filter(Post.active==True).order_by(func.ST_Distance(Post.location,func.Geometry(func.ST_GeomFromText('POINT({} {})'.format(lon, lat))))).all()

    l=[{"message":i.message,"location":str(i.location),"created_on":timeago.format(datetime.datetime.now(datetime.timezone.utc),i.created_on)} for i in q]
    obj={}
    obj["success"]=True
    obj['results'] = l[0:10]
    # return obj
    return jsonify(obj)#{"message":q.message,"location":str(q.location),"created_on":timeago.format(datetime.datetime.now(),q.created_on)}