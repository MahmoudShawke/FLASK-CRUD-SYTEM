from  flask import render_template,Blueprint,redirect, request, render_template
import pymongo

all=Blueprint('all',__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Day2"]


@all.route('/home')
def render():
    trainers = mydb.Trainers.find({})
    return render_template('traine/index.html',tr=trainers)