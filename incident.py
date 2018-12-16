from flask import Flask, request, make_response, jsonify
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

app = Flask(__name__)

#Status Codes
STATUS_CODES = dict(success = 200, created = 201, no_content = 204, bad_request = 400, 
                    not_found = 404, not_implemented = 501)

#Data to be served over the API ---------------------------------------------------------
RED_FLAGS = [{
            "id" : 1, 
            "title" : "Corruption at Ministry of Eduction",
            "createdOn" : get_timestamp(),
            "createdBy" : 5,
            "type" : "red-flag",
            "location" : "LAT234, LOG342",
            "status" : "draft",
            "images" : ["img/image1.jpg", "img/image2.jpg"],
            "videos" : ["vid/video1.mp4", "vid/video2.jpg"],
            "comment" : "It is a long established fact that a reader will be distracted by the readable content of a page"
    },
    {
            "id" : 2, 
            "title" : "Corruption at NSSF",
            "createdOn" : get_timestamp(),
            "createdBy" : 5,
            "type" : "red-flag",
            "location" : "LAT234, LOG342",
            "status" : "draft",
            "images" : ["img/image1.jpg", "img/image2.jpg"],
            "videos" : ["vid/video1.mp4", "vid/video2.jpg"],
            "comment" : "It is a long established fact that a reader will be distracted by the readable content of a page"
    },
    {
            "id" : 3, 
            "title" : "Corruption by a UNRA offical",
            "createdOn" : get_timestamp(),
            "createdBy" : 5,
            "type" : "red-flag",
            "location" : "LAT234, LOG342",
            "status" : "draft",
            "images" : ["img/image1.jpg", "img/image2.jpg"],
            "videos" : ["vid/video1.mp4", "vid/video2.jpg"],
            "comment" : "It is a long established fact that a reader will be distracted by the readable content of a page"
    }]
  

#Add New Red Flag -------------------------------------------------------------------------
@app.route("/api/v1/red_flags/", methods=["POST"])
def add_red_flag():
    """ Should return Status Code:201 if a Red Flag is created"""
    if request.content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()   
    new_red_flag = {    
        "id" : 4,
        "title" : data["title"],
        "createdOn" : get_timestamp(),
        "createdBy" : data["createdBy"],
        "type" : data["type"],
        "location" : data["location"],
        "status" : "draft",
        "images" : data["images"],
        "videos" : data["videos"],
        "comment" : data["comment"]
    }

    RED_FLAGS.append(new_red_flag)
    return jsonify({"status" : STATUS_CODES["created"], "data" : [{
                                        "id" :  new_red_flag["id"], 
                                        "message" : "Created red-flag record with id {}".format(new_red_flag["id"])
                                        }]
                                    }), STATUS_CODES["created"]

#Get all Red Flags ------------------------------------------------------------------------
@app.route("/api/v1/red_flags/", methods=["GET"])
def get_all_red_flags():
    """ Should return Status Code:200 along with all the Red Flags |
        Code:404 if there are no Red Flags
    """
    return jsonify({"status" : 200, "data" : RED_FLAGS}) 

#Get specific Red Flag by id ---------------------------------------------------------------
@app.route("/api/v1/red_flags/<int:id>/", methods=["GET"])
def get_specific_red_flag(id):
    """ Should return Status Code:200 along with the requested Red Flag |
        Code:404 if there is no Red Flag for the specified id
    """
    for red_flag in RED_FLAGS:
        if red_flag["id"] == id:
            return jsonify({"status" : STATUS_CODES["success"], "data" : red_flag })
    return jsonify({
                    "status" : STATUS_CODES["not_found"], 
                    "error" : "Red flag with id {} does not exit".format(id)
                    }), STATUS_CODES["not_found"]
    

#Edit Specific Red Flag ------------------------------------------------------------------
@app.route("/api/v1/red_flags/<int:id>/", methods=["PATCH"])
def edit_specific_red_flag(id):
    """ Should return Status Code:200 along with the requested Red Flag |
        Code:404 if there is no Red Flag for the specified id
    """
    if request.content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()
    for red_flag in RED_FLAGS:
        if red_flag["id"] == id:    
            red_flag["title"] = data["title"]
            red_flag["images"] = data["images"]
            red_flag["videos"] = data["videos"]
            red_flag["comment"] = data["comment"]

            return jsonify({"status" : STATUS_CODES["success"], "data" : [{
                                                "id" :  red_flag["id"], 
                                                "message" : "Updated red-flag comment for id {}".format(red_flag["id"])
                                                }]
                                            }), STATUS_CODES["success"]
    return jsonify({
                    "status" : STATUS_CODES["not_found"], 
                    "error" : "No record found for red-flag with id {}".format(id)
                    }), STATUS_CODES["not_found"]

#Delete Specific Red Flag ----------------------------------------------------------------
@app.route("/api/v1/red_flags/<int:id>/", methods=["DELETE"])
def delete_specific_red_flag(id):
    """ Should return Status Code:200 along with the requested Red Flag |
        Code:404 if there is no Red Flag for the specified id
    """
    
    for red_flag in RED_FLAGS:
        if red_flag["id"] == id:
            del RED_FLAGS[RED_FLAGS.index(red_flag)]
            return jsonify({"status" : 200, 
                    "data" : [{
                        "id" : id,
                        "message" : "red-flag record has been deleted for id {}".format(id)
                        }]
                    })
    return jsonify({
                    "status" : STATUS_CODES["not_found"], 
                    "error" : "No record found for red-flag with id {}".format(id)
                    }), STATUS_CODES["not_found"]

#------------------------------------------------------------------------------------------

#Start Server------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
    
    