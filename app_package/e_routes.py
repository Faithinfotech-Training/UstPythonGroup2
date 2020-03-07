from flask import render_template, flash, redirect,url_for
from app_package import app, mongo
from app_package.e_forms import EnquiryForm, UpdateEnquiryForm
check=True
e_id=0 

@app.route("/")
def index():
    return redirect(url_for("view_enquiry"))

@app.route("/add_enquiry", methods=["GET","POST"])
def add_enquiry():
    global e_id,check
    form=EnquiryForm()
    if form.validate_on_submit():
        fields=["_id","name","mobno","email","yearofpass","highqual","location","prefercourse","source","status"]
        e_id+=1
        values=[e_id,form.name.data,form.mobno.data,form.email.data,form.yearofpass.data,form.highqual.data,form.location.data,form.prefercourse.data,form.source.data,form.status.data]
        enquiry=dict(zip(fields,values))
        enq_col=mongo.db.enquiries 
        if check:
            check=False
            if enq_col.count()==0:
                e_id=0
            else:
                e=enq_col.find().sort("_id",-1).limit(1)
                tmp=e.next()
                e_id=tmp["_id"]
        e_id+=1
        enquiry["_id"]=e_id
        
        tmp=enq_col.insert_one(enquiry)
        if tmp.inserted_id==e_id:
            flash("enquiry added")
            return redirect(url_for("view_enquiry"))
        else:
            flash("problem adding enquiry")
            return redirect(url_for("add_enquiry"))
            
    else:            
        return render_template("add_enquiry.html",form=form)   
        
        
      
@app.route("/view_enquiry")
def view_enquiry():
    enq_col=mongo.db.enquiries
    enquiries=enq_col.find()
    return render_template("view_enquiry.html",enquiries=enquiries)


@app.route("/update_enquiry/<int:enqid>", methods=["GET","POST"])
def update_enquiry(enqid):
    form=UpdateEnquiryForm()
    enq_col=mongo.db.enquiries
    enquiry=enq_col.find_one({"_id":enqid})
    if form.validate_on_submit():
        values=dict()
        enq_col=mongo.db.enquiries
        if form.name.data!="":values["name"]=form.name.data
        if form.mobno.data!="":values["mobno"]=form.mobno.data
        if form.email.data!="":values["email"]=form.email.data 
        if form.yearofpass.data!="":values["yearofpass"]=form.yearofpass.data
        if form.highqual.data!="":values["highqual"]=form.highqual.data
        if form.location.data!="":values["location"]=form.location.data
        if form.prefercourse.data!="":values["prefercourse"]=form.prefercourse.data
        if form.source.data!="":values["source"]=form.source.data
        if form.status.data!="":values["status"]=form.status.data
        query={"_id":enqid}
        new_data={"$set":values}
        enq_col.update_one(query,new_data)
        flash("enquiry details modified")
        return redirect(url_for("view_enquiry")) 
    else:
        return render_template("update_enquiry.html",form=form,enquiry=enquiry)

    

    
                   
