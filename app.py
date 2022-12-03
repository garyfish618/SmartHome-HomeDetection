from flask import Flask, jsonify, request
from database_client import db
from forms.register_address_form import RegisterAddressForm
import find_device
import threading

app = Flask(__name__)

detection_worker = threading.Thread(target=find_device.start_scanning)
detection_worker.start()


@app.route("/register/", methods=['POST'])
def register():
    if request.method == 'POST':
        form = RegisterAddressForm(request.args)
        if form.validate:
            db.hosts_to_watch.insert_one(form.data)
            return jsonify(isError=False, message="Success")
        else:
            return jsonify(isError=True, message="Invalid data"), 400

