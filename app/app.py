from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper()

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    # Return template and data
    return render_template("about_us.html")

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau.html")

@app.route("/ml")
def ml():
    # Return template and data
    return render_template("ml.html")

@app.route("/makePredictions", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print(content)

    # parse
    Base_Exp = float(content["Base_Exp"])
    Attack = float(content["Attack"])
    Sp_Atk = float(content["Sp_Atk"])
    Defense = float(content["Defense"])
    Sp_Def = float(content["Sp_Def"])
    HP = float(content["HP"])



    preds = modelHelper.makePredictions(Attack, Sp_Atk, Defense, Sp_Def, HP, Base_Exp)
    return(jsonify({"ok": True, "prediction": str(preds)}))


#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
