from flask import Flask, request, render_template
import json
import os
from urllib.parse import unquote_plus
from delay_sub_recharge import move_shipment
from product_creator import product_creator
from address_tools import get_address
from flask_mysqldb import MySQL
from PIL import Image
import uuid

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'gbenneth'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Database123!'
app.config['MYSQL_DATABASE_DB'] = 'gbenneth$requests'
app.config['MYSQL_DATABASE_HOST'] = 'gbenneth.mysql.pythonanywhere-services.com'
mysql.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        images = request.files.getlist("image")
        project_number = str(uuid.uuid4().int)
        os.makedirs(os.path.join(app.root_path,'static', project_number))
        resized_images=[]
        for image in images:
            original_filename = image.filename
            image.save(os.path.join(app.root_path,'static', project_number, original_filename))
            resized_image = Image.open(image)
            resized_image = resized_image.convert("RGB")
            resized_image = resized_image.resize((200, 200))
            filename = f'resized_image_{image.filename}'
            resized_image.save(os.path.join(app.root_path, 'static', project_number, filename))
            resized_images.append(filename)
        return render_template('index.html', resized_images=resized_images,project_number=project_number)
    return render_template('index.html')

@app.route('/results', methods=['GET','POST'])
def create_product():
    if request.get_json() is None:
        return "Error: No data received"

    data = request.get_json()
    project_num = data['data']['project_num']
    product_data = data['data']['product_data']
    new_files, csv_file = product_creator(project_num,product_data)
    return render_template('result.html', new_files=new_files,csv_file=csv_file,project_number=project_num)
