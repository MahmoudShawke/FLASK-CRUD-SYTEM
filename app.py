from flask import Flask
from flask import Flask,redirect, request, render_template
from views.insert import home
from views.update import updatee
from views.dashboard import all
from views.delete import deletes
import pymongo



app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(updatee)
app.register_blueprint(all)
app.register_blueprint(deletes)


# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["Day2"]
# trainers=mydb.Trainers.find({})
# mycol = mydb["Trainers"]
#
# def next_id():
#     x = mydb.Trainers.find({}).sort("_id", -1).limit(1)
#     id = 0
#     for i in x:
#         id = i['_id']
#     return id+1 if x!=0 else redirect('/home')
#
#
# users =[]
# @app.route('/')
# def hello_world():
#     return render_template('temp.html')
#
# @app.route('/home')
# def render():
#     trainers = mydb.Trainers.find({})
#     return render_template('traine/index.html',tr=trainers)
#
# @app.route('/insert',methods=["POST","GET"])
# def insert():  # put application's code here
#     if request.method =='GET':
#         return render_template('traine/insert.html')
#     else:
#
#         uname = request.form.get('Username')
#         uage = request.form.get('National')
#         course = request.form.get('Course')
#         mycol = mydb["Trainers"]
#
#
#         mycol.insert_one({'_id':next_id(),"Username": uname, "National": uage, "Course": course})
#         return redirect('/home')
#
# @app.route('/delete/<int:id>')
# def delete(id):
#     mycol = mydb["Trainers"]
#     mycol.delete_one({'_id': id})
#
#
#     return redirect('/home')
#
# @app.route('/update/<int:id>',methods=["POST","GET"])
# def update(id):
#     mycol = mydb["Trainers"]
#     if request.method == 'POST':
#
#         uname = request.form.get('Username')
#         uage = request.form.get('National')
#         course = request.form.get('Course')
#         mycol.update_one({"_id":id},{"$set": {"Username": uname, "National": uage, "Course": course}})
#
#         return redirect('/home')
#     else:
#
#         trainers =list( mydb.Trainers.find({'_id':id}))
#         return render_template('traine/update.html', tr=trainers)
#

if __name__ == '__main__':
    app.run(debug=True)
