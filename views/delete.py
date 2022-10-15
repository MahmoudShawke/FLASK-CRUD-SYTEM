from  flask import render_template,Blueprint,redirect, request, render_template
import pymongo

deletes=Blueprint('delete',__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Day2"]
trainers=mydb.Trainers.find({})
mycol = mydb["Trainers"]
@deletes.route('/delete/<int:id>')
def delete(id):
    mycol = mydb["Trainers"]
    mycol.delete_one({'_id': id})


    return redirect('/home')