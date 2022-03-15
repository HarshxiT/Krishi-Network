from flask import jsonify, request, flash
from run import app;
from apps.post.models.post_info import Post
from run import db

@app.route("/createPost", methods=[ "POST"])
def createEmployee():
   #  form = EmployeeForm(request.form)
   form=request.get_json()
   employees = Post.query.all()
   # if form.validate_on_submit():
   employee = Post(message=form["message"], location='POINT('+form["location"]+')')
   db.session.add(employee)
   db.session.commit()
   db.session.refresh(employee)
   db.session.commit()
   flash("Added Employee Successfully")
   return jsonify({'success': True})