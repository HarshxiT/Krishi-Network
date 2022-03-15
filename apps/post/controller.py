from flask import jsonify, request, flash
import datetime
from sqlalchemy import func
from apps.post.models import Post
from run import db
import timeago
from werkzeug.exceptions import HTTPException
def createPost():
   try:
      form=request.get_json()
      employee = Post(message=form["message"], location='POINT('+form["location"]+')')
      db.session.add(employee)
      db.session.commit()
      db.session.refresh(employee)
      db.session.commit()
      flash("Added Employee Successfully")
      return jsonify({'success': True}),200
   except Exception as e:
      raise Exception("Something bad happened")
      


def getPost():
   try:
      args = request.args
      lon = str(args.get('lon'))
      lat = str(args.get('lat'))
      # if None in (lon, lat):
      #     raise Exception("Invalid")

      q = db.session.query(Post.message,Post.location,Post.created_on).filter(Post.active==True).order_by(func.ST_Distance(Post.location,func.Geometry(func.ST_GeomFromText('POINT({} {})'.format(lon, lat))))).all()

      l=[{"message":i.message,"location":str(i.location),"created_on":timeago.format(datetime.datetime.now(),i.created_on)} for i in q]
      obj={}
      obj["success"]=True
      obj['results'] = l[0:10]
      return jsonify(obj),200
   except Exception as e:
      raise Exception("Something bad happened")