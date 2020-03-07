from flask import redirect,render_template,flash,url_for
from wtforms import ValidationError
from app_package import app,mongo
from app_package.resforms import AddResourceForm,UpdateResourceForm

check=True
r_id=0

# @app.route("/")
# def menu():
#     return redirect(url_for("view_resource"))

@app.route("/add_resource",methods=['GET','POST'])
def add_resource():
    global r_id,check
    form=AddResourceForm()
    if form.validate_on_submit():
        fields=["_id","resourcename","seatcapacity","usetype","rent","status"]
        res_col=mongo.db.resources
        if check:
            check=False
            if res_col.count()==0:
                r_id=0
            else:
                res=res_col.find().sort("_id",-1).limit(1)
                tmp=res.next()
                r_id=tmp["_id"]
        r_id+=1
        values=[r_id,form.resourcename.data,form.seatcapacity.data,form.usetype.data,form.rent.data,"available"]
        resource=dict(zip(fields,values))
        name=res_col.find_one({"resourcename":form.resourcename.data})
        if not bool(name):
            if  form.rent.data>0:
                tmp=res_col.insert_one(resource)
            else:
                flash("please enter valid data")
                return redirect(url_for('add_resource'))
            if tmp.inserted_id==r_id:
                flash("resource added")
                return redirect(url_for("menu"))
            else:
                flash("problem adding resource")    
            
                return redirect(url_for("add_resource"))
        else:
            flash("resource already exist")
            return redirect(url_for('add_resource'))
    else:
        return render_template("add_resource.html",form=form)

@app.route("/view_resource",methods=["GET","POST"])
def view_resource():
    res_col=mongo.db.resources
    res=res_col.find()
    return render_template("view_resource.html",res=res)

@app.route("/modify_resource/<int:a>",methods=["GET","POST"])      
def modify_resource(a):
    form=UpdateResourceForm()
    values=dict()
    res_col=mongo.db.resources
    usr=res_col.find_one({"_id":a})
    if form.validate_on_submit():
        
       
        if form.rent.data!="" and form.rent.data>0: values["rent"]=form.rent.data
        else:
            flash("please enter valid rent")
            return render_template("modify_resource.html",form=form,usr=usr)
        if form.status.data!="":values["status"]=form.status.data
        if form.usetype.data!="":values["usetype"]=form.usetype.data 
        new_data={"$set":values}
        query={"_id":a}
        res_col=mongo.db.resources
        res_col.update_one(query,new_data)
        flash("Resource updated")
        return redirect(url_for("view_resource"))
    else:
        
        return render_template("modify_resource.html",form=form,usr=usr)