from flask import render_template, flash, redirect, url_for
from app_package import app,mongo

from app_package.cforms import AddCourseForm,UpdateCourseForm
c_id=0
check=True
@app.route("/", methods=["GET","POST"])
def index():
    return redirect(url_for("display_course"))
       

@app.route("/coursemenu")  
def coursemenu():
    return render_template("coursemenu.html")
     
@app.route("/logout")
def logout():
    return redirect(url_for("index")) 

@app.route("/addcourse",methods=["GET","POST"])
def addcourse():
	global c_id,check
	form=AddCourseForm()
	if form.validate_on_submit():
		fields=["_id","name","duration","fee","status","description"]
		course_col=mongo.db.courses
		if check:
			check=False
			if course_col.count()==0:
				c_id=0
			else:
				cc=course_col.find().sort("_id",-1).limit(1)
				tmp=cc.next()
				c_id=tmp["_id"]
		c_id+=1
		course=course_col.find_one({"name":form.name.data})
		if not bool(course):
			values=[c_id,form.name.data,form.duration.data,form.fee.data,form.status.data,form.description.data]
			course=dict(zip(fields,values))
			course_col=mongo.db.courses
			tmp=course_col.insert_one(course)		
			if tmp.inserted_id==c_id:
				flash("course added")
				return redirect(url_for("display_course"))
			else:
				flash("Problem adding courses")
				return redirect(url_for("index"))
		else:
			flash("Course name already exists...")
			return redirect(url_for("addcourse"))	
	else:
		return render_template("add_course.html",form=form)

@app.route("/display_course")
def display_course():
	course_col=mongo.db.courses
	course=course_col.find()
	return render_template("display_course.html",course=course)



@app.route("/update_course/<int:a>",methods=["GET","POST"])
def update_course(a):
	form=UpdateCourseForm()
	course_col=mongo.db.courses
	usr=course_col.find_one({"_id":a})
	if form.validate_on_submit():
		values=dict()
		if form.duration.data!="":values["duration"]=form.duration.data	
		if form.fee.data!="":values["fee"]=form.fee.data	
		if form.status.data!="":values["status"]=form.status.data	
		query={"_id":a}
		course_col=mongo.db.courses
		#usr=course_col.find_one({"_id":a})
		new_data={"$set":values}
		course_col.update_one(query,new_data)
		flash("course updated")
		return redirect(url_for("display_course"))
	else:
		return render_template("update_course.html",form=form,usr=usr)

