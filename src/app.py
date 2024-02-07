from flask import Flask, request, make_response, jsonify
from werkzeug.utils import secure_filename
from process import Process

app = Flask(__name__)

@app.route('/')
def mainpage():
    return "<p>Nothing to request here...</p>"


@app.route('/get_result', methods=['GET', 'POST'])
def result():
    try:
        file = request.files['img']
        filename = secure_filename(file.filename)
        saved_path = "../images/"+filename
        file.save(saved_path)
    except:
        resp = make_response("Bad Request", 400)
        resp.headers['X-Something'] = 'A value'
        return resp
    try:
        processor = Process(saved_path)
    except:
        resp = make_response("Server Error", 500)
        resp.headers['X-Something'] = 'A value'
        return resp
    data = {'emotion': processor.process()}
    return jsonify(data), 200

if __name__ == '__main__':
   app.run(debug=True)