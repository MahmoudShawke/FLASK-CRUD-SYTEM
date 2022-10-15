from  flask import render_template,Blueprint,redirect, request, render_template
import pymongo

home=Blueprint('homepage',__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Day2"]
trainers=mydb.Trainers.find({})
mycol = mydb["Trainers"]
def next_id():
    x = mydb.Trainers.find({}).sort("_id", -1).limit(1)
    id = 0
    for i in x:
        id = i['_id']
    return id+1 if x!=0 else redirect('/home')



@home.route('/insert',methods=["POST","GET"])
def insert():  # put application's code here
    if request.method =='GET':
        return render_template('traine/insert.html')
    else:

        uname = request.form.get('Username')
        uage = request.form.get('National')
        course = request.form.get('Course')
        mycol = mydb["Trainers"]


        mycol.insert_one({'_id':next_id(),"Username": uname, "National": uage, "Course": course})
        return redirect('/home')
    