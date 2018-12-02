from flask import Flask, request, make_response, jsonify
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

app = Flask(__name__)

#Data to be served over the API ---------------------------------------------------------
RED_FLAGS = [{
            "id" : 1, 
            "title" : "Corruption at Ministry of Eduction",
            "createdOn" : get_timestamp(),
            "createdBy" : 5,
            "type" : "red-flag",
            "location" : "LAT234, LOG342",
            "status" : "draft",
            "Images" : ["img/image1.jpg", "img/image2.jpg"],
            "Videos" : ["vid/video1.mp4", "vid/video2.jpg"],
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
            "Images" : ["img/image1.jpg", "img/image2.jpg"],
            "Videos" : ["vid/video1.mp4", "vid/video2.jpg"],
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
            "Images" : ["img/image1.jpg", "img/image2.jpg"],
            "Videos" : ["vid/video1.mp4", "vid/video2.jpg"],
            "comment" : "It is a long established fact that a reader will be distracted by the readable content of a page"
    }]
  

#Add New Red Flag -------------------------------------------------------------------------
@app.route("/api/v1/red_flags/", methods=["POST"])
def add_red_flag():
    """ Should return Status Code:201 if a Red Flag is created"""

    new_red_flag = {    
        "id" : 4,
        "title" : request.form["title"],
        "createdOn" : get_timestamp(),
        "createdBy" : request.form["user-id"],
        "type" : request.form["incident-type"],
        "location" : request.form["location"],
        "status" : "draft",
        "Image" : request.form["image"],
        "Video" : request.form["video"],
        "comment" : request.form["comment"]
    }

    RED_FLAGS.append(new_red_flag)
    return jsonify({"status" : 201, "data" : [{
                                        "id" :  new_red_flag["id"], 
                                        "message" : "Created red-flag record with id {}".format(new_red_flag["id"])
                                        }]
                                    })
    #return jsonify({"status" : 404, "data" : "Not authorized"})

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
            return jsonify({"status" : 200, "data" : red_flag })
    return jsonify({"Status" : 404, "Message" : "Red flag with id {} does not exits".format(id)})
    

#Edit Specific Red Flag ------------------------------------------------------------------
@app.route("/api/v1/red_flags/<int:id>/", methods=["PATCH"])
def edit_specific_red_flag(id):
    """ Should return Status Code:200 along with the requested Red Flag |
        Code:404 if there is no Red Flag for the specified id
    """
    for red_flag in RED_FLAGS:
        if red_flag["id"] == id:    
            red_flag["title"] = request.form["title"]
            red_flag["Image"] = request.form["image"]
            red_flag["Video"] = request.form["video"]
            red_flag["comment"] = request.form["comment"]

            return jsonify({"status" : 201, "data" : [{
                                                "id" :  red_flag["id"], 
                                                "message" : "Updated red-flag comment for id {}".format(red_flag["id"])
                                                }]
                                            })
    return jsonify({"status" : 404, 
                    "data" : [{
                        "id" : id,
                        "message" : "No record found for red-flag with id {}".format(id)
                        }]
                    })

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
    return jsonify({"status" : 404, 
                    "data" : [{
                        "id" : id,
                        "message" : "No record found for red-flag with id {}".format(id)
                        }]
                    })

    
    pass
#------------------------------------------------------------------------------------------

#Start Server------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
    
    