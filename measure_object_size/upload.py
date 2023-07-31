from flask import Flask, render_template, request, redirect, url_for
# from flask_restful import Resource, Api, reqparse
import os
import pandas as pd
from measure_object_size import measurement_driver
import sys

app = Flask(__name__)

# Define the route for the upload page


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/service')
def service():
    return render_template('service.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['file']

        # Save the file to the uploads folder
        file.save(os.path.join('uploads', file.filename))

        # Redirect to the uploaded file's URL
        return redirect(url_for('measure_dim', filename=file.filename))

    # Render the upload form template
    return render_template('upload.html')


@app.route('/measure/<filename>')
def measure_dim(filename):
    op_path = measurement_driver(filename)
    return render_template('output.html', output_image=op_path)


# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     # return f'<img src="{url_for("static", filename="images/" + filename)}">'
#     return f'<img src="{url_for("upload", filename="outputs/" + filename)}">'


# class Users(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()

#         parser.add_argument('userId', required=True)  # add args
#         parser.add_argument('name', required=True)
#         parser.add_argument('city', required=True)

#         args = parser.parse_args()  # parse arguments to dictionary

#         # create new dataframe containing new values
#         new_data = pd.DataFrame({
#             'userId': args['userId'],
#             'name': args['name'],
#         })

#         return {'data': new_data}, 200

if __name__ == '__main__':
    app.run(debug=True)
