#API

from flask import Flask

# ----------------------
# $$$$$$$ FLASK GET $$$$$$$$
# ----------------------

app=Flask(__name__)

@app.route('/', methods=['GET'])
def default():
    return '''<h1>API DEL PROYECTO "VIVIR EN MADRID" DE @CRISTIDATAS</h1>
<p>Para conseguir el json añadir a la url get_token?id=</p>'''

@app.route('/get_token', methods=['GET'])
def get_json():
    token=None
    # Get json fullpath
    datos_limpios=os.path.dirname(__file__)+"\\..\\..\\resources\\json\\output\\datos_limpios.json"
    # Load json from file
    with open (datos_limpios,"r") as json_file_readed:
        limpios=json.load(json_file_readed)
    if "id" in request.args:
        token=str(request.args["id"])
    if token=="J51931529":
        return limpios