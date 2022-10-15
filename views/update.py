from  flask import render_template,Blueprint,redirect, request, render_template
import pymongo

updatee=Blueprint('update',__name__)

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


@updatee.route('/update/<int:id>',methods=["POST","GET"])
def update(id):
    mycol = mydb["Trainers"]
    if request.method == 'POST':

        uname = request.form.get('Username')
        uage = request.form.get('National')
        course = request.form.get('Course')
        mycol.update_one({"_id":id},{"$set": {"Username": uname, "National": uage, "Course": course}})

        return redirect('/home')
    else:

        trainers =list( mydb.Trainers.find({'_id':id}))
        return render_template('traine/update.html', tr=trainers)
