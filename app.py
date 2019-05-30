from flask import Flask, render_template, request, redirect
import os
import pymongo
from bson import ObjectId
from werkzeug.utils import secure_filename


# UPLOAD_FOLDER = '/static/images'
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

MONGODB_URL= 'mongodb://energize:mongodb92@cluster0-shard-00-00-4z9sv.mongodb.net:27017,cluster0-shard-00-01-4z9sv.mongodb.net:27017,cluster0-shard-00-02-4z9sv.mongodb.net:27017/receipedb?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'
 
connection = pymongo.MongoClient(MONGODB_URL)

collection = connection['receipedb']['all_receipe']



@app.route('/uploaded')
def uploaded():
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        connection.save_file(profile_image.filename)

@app.route('/')
def home():
    allrec = connection['receipedb']['all_receipe']
    found = allrec.find({})
    return render_template('index.html', all_receipe=found)
    
@app.route('/add_new', methods=['GET', 'POST'])
def add_new():
    if request.method == 'GET':
        
        food_origins = connection['receipedb']['food_origins']
        found = food_origins.find({})
        
        dish = connection['receipedb']['dish_type']
        tound = dish.find({})
        
        diet = connection['receipedb']['diet_req']
        sound = diet.find({})
        
        diff = connection['receipedb']['diff_lvl']
        hound = diff.find({})
        
        return render_template('add_new.html', food_origins=found, dish_type=tound, diet_req=sound, diff_lvl=hound)
    else:
        #
        # f = request.files['file']
        # f.save(secure_filename(f.filename))
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'], f))
        #
        title = request.form['title']
        author = request.form['author']
        origins = request.form['origins']
        dish = request.form['dish']
        diet = request.form['diet']
        diff = request.form['difficulty']
        inlist = request.form['inlist']
        instruct = request.form['instruct']
        receipe_collection = connection['receipedb']['all_receipe']
        receipe_collection.insert({
            'title': title,
            'author': author,
            'origins': origins,
            'dish': dish,
            'diet': diet,
            'difficulty': diff,
            'inlist': inlist,
            'instruct': instruct
        })
        
        return redirect('/')
        
@app.route('/edit/<allreceipe_id>', methods=['GET','POST'])
def edit(allreceipe_id):
    receipe_collection = connection['receipedb']['all_receipe']
    if request.method == 'GET':
        receipe_from_db = receipe_collection.find_one({
        '_id': ObjectId(allreceipe_id)    
        })
        food_origins = connection['receipedb']['food_origins']
        found = food_origins.find({})
        
        dish = connection['receipedb']['dish_type']
        tound = dish.find({})
        
        diet = connection['receipedb']['diet_req']
        sound = diet.find({})
        
        diff = connection['receipedb']['diff_lvl']
        hound = diff.find({})
        
        
        return render_template('edit.html', all_receipe=receipe_from_db, food_origins=found, dish_type=tound, diet_req=sound, diff_lvl=hound)
    else:
        title = request.form['title']
        author = request.form['author']
        origins = request.form['origins']
        dish = request.form['dish']
        diet = request.form['diet']
        diff = request.form['difficulty']
        inlist = request.form['inlist']
        instruct = request.form['instruct']
        
        receipe_collection.update({
        '_id': ObjectId(allreceipe_id)
        }, {
            '$set': {
                'title': title,
                'author': author,
                'origins': origins,
                'dish': dish,
                'diet': diet,
                'difficulty': diff,
                'inlist': inlist,
                'instruct': instruct,
            }
        })
        
        return redirect('/')

@app.route('/delete/<allreceipe_id>', methods=['GET', 'POST'])
def delete(allreceipe_id):
    if (request.method=='GET'):
        return """
         <script>
        function goBack() {
          window.history.back();
        }
        </script>
        <form method='post'>
        <p>Are you sure you want to delete?</p>
        <input type='submit' value='YES'></input>
        <button onclick="goBack()">NO</button>
        </form>
        """
    else:
        receipe_collection = connection['receipedb']['all_receipe']
        receipe_collection.remove({
            '_id':ObjectId(allreceipe_id)
        })
    return redirect('/')


@app.route('/search', methods=['GET', 'POST'])
def search():
    receipe_collection = connection['receipedb']['all_receipe']
    
    food_origins = connection['receipedb']['food_origins']
    found = food_origins.find({})
    
    dish = connection['receipedb']['dish_type']
    tound = dish.find({})
    
    diet = connection['receipedb']['diet_req']
    sound = diet.find({})
    
    diff = connection['receipedb']['diff_lvl']
    hound = diff.find({})
        
    if (request.method =='GET'):
        
        return render_template('search.html', diff_lvl=hound, food_origins=found, dish=tound, diet=sound)
        
    else:
        
        origins = request.form['origins']
        dish = request.form['dish']
        diet = request.form['diet']
        diff = request.form['difficulty']
        receipe_collection = connection['receipedb']['all_receipe']
         
        allrec = receipe_collection.find({
                # 'title': title,
                'origins': origins,
                'dish': dish,
                'diet': diet,
                'difficulty': diff
        })

        
        return render_template('search.html', receipe_collection=allrec, diff_lvl=hound, food_origins=found, dish=tound, diet=sound)
        
@app.route('/filter1', methods=['GET', 'POST'])
def food():
    receipe_collection = connection['receipedb']['all_receipe']
    
    food_origins = connection['receipedb']['food_origins']
    found = food_origins.find({})
    
    if (request.method =='GET'):
        return render_template('filter1.html', food_origins=found)
        
    else:
         origins = request.form['origins']
         receipe_collection = connection['receipedb']['all_receipe']
         allrec = receipe_collection.find({'origins': origins,})
         
         return render_template('filter1.html', receipe_collection=allrec, food_origins=found)
        
@app.route('/filter2', methods=['GET', 'POST'])
def dish():
    receipe_collection = connection['receipedb']['all_receipe']
    
    dish = connection['receipedb']['dish_type']
    tound = dish.find({})
    if (request.method =='GET'):
        return render_template('filter2.html', dish=tound)
        
    else:
         dish = request.form['dish']
         receipe_collection = connection['receipedb']['all_receipe']
         allrec = receipe_collection.find({'dish': dish,})
         
         return render_template('filter2.html', receipe_collection=allrec, dish=tound)

@app.route('/filter3', methods=['GET', 'POST'])
def diet():
    receipe_collection = connection['receipedb']['all_receipe']
    
    diet = connection['receipedb']['diet_req']
    sound = diet.find({})
    if (request.method =='GET'):
        return render_template('filter3.html', diet=sound)
        
    else:
         diet = request.form['diet']
         receipe_collection = connection['receipedb']['all_receipe']
         allrec = receipe_collection.find({'diet': diet,})
         
         return render_template('filter3.html', receipe_collection=allrec, diet=sound)

@app.route('/filter4', methods=['GET', 'POST'])
def diff():
    receipe_collection = connection['receipedb']['all_receipe']
    
    diff = connection['receipedb']['diff_lvl']
    hound = diff.find({})
    if (request.method =='GET'):
        return render_template('filter4.html', diff=hound)
        
    else:
         diff = request.form['difficulty']
         receipe_collection = connection['receipedb']['all_receipe']
         allrec = receipe_collection.find({'difficulty': diff,})
         
         return render_template('filter4.html', receipe_collection=allrec, diff=hound)
         

@app.route('/display/<allreceipe_id>', methods=['GET'])
def display(allreceipe_id):
    receipe_collection = connection['receipedb']['all_receipe']
    
    receipe_from_db = receipe_collection.find_one({'_id': ObjectId(allreceipe_id)})
    return render_template('display.html', all_receipe=receipe_from_db)
    
@app.route('/string', methods=['GET', 'POST'])
def string():
    receipe_collection = connection['receipedb']['all_receipe']
    if (request.method =='GET'):
        found=receipe_collection.find( { '$text': { '$search:' }} )
        
        return render_template('string.html', receipe_collection=found )
    
    else:
        return
    



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)    