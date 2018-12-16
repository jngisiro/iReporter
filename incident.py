from flask import Flask, make_response, jsonify
import helper

app = Flask(__name__)

#Add New Red Flag -------------------------------------------------------------------------
@app.route("/api/v1/red_flags/", methods=["POST"])
def add_red_flag():
    """ Should return Status Code:201 if a Red Flag is created"""
    data = helper.get_request_json() 
    new_red_flag = {    
        "id" : 4,
        "title" : data["title"],
        "createdOn" : helper.get_timestamp(),
        "createdBy" : data["createdBy"],
        "type" : data["type"],
        "location" : data["location"],
        "status" : "draft",
        "images" : data["images"],
        "videos" : data["videos"],
        "comment" : data["comment"]
    }

    helper.RED_FLAGS.append(new_red_flag)
    return jsonify({"status" : helper.STATUS_CODES["created"], "data" : [{
                                        "id" :  new_red_flag["id"], 
                                        "message" : "Created red-flag record with id {}".format(new_red_flag["id"])
                                        }]
                                    }), helper.STATUS_CODES["created"]

#Get all Red Flags ------------------------------------------------------------------------
@app.route("/api/v1/red_flags/", methods=["GET"])
def get_all_red_flags():
    """ Should return Status Code:200 along with all the Red Flags |
        Code:404 if there are no Red Flags
    """
    return jsonify({"status" : 200, "data" : helper.RED_FLAGS}) 

#Get specific Red Flag by id ---------------------------------------------------------------
@app.route("/api/v1/red_flags/<int:id>/", methods=["GET"])
def get_specific_red_flag(id):
    """ Should return Status Code:200 along with the requested Red Flag |
        Code:404 if there is no Red Flag for the specified id
    """
    for red_flag in helper.RED_FLAGS:
        if red_flag["id"] == id:
            return jsonify({"status" : helper.STATUS_CODES["success"], "data" : red_flag })
    return helper.error_404_message(id)
    

#Edit Specific Red Flag ------------------------------------------------------------------
@app.route("/api/v1/red_flags/<int:id>/", methods=["PATCH"])
def edit_specific_red_flag(id):
    """ Should return Status Code:200 along with the requested Red Flag |
        Code:404 if there is no Red Flag for the specified id
    """
    data = helper.get_request_json()
    for red_flag in helper.RED_FLAGS:
        if red_flag["id"] == id:    
            red_flag["title"] = data["title"]
            red_flag["images"] = data["images"]
            red_flag["videos"] = data["videos"]
            red_flag["comment"] = data["comment"]

            return jsonify({"status" : helper.STATUS_CODES["success"], "data" : [{
                                                "id" :  red_flag["id"], 
                                                "message" : "Updated red-flag comment for id {}".format(red_flag["id"])
                                                }]
                                            }), helper.STATUS_CODES["success"]
    return helper.error_404_message(id)

#Delete Specific Red Flag ----------------------------------------------------------------
@app.route("/api/v1/red_flags/<int:id>/", methods=["DELETE"])
def delete_specific_red_flag(id):
    """ Should return Status Code:200 along with the requested Red Flag |
        Code:404 if there is no Red Flag for the specified id
    """
    
    for red_flag in helper.RED_FLAGS:
        if red_flag["id"] == id:
            del helper.RED_FLAGS[helper.RED_FLAGS.index(red_flag)]
            return jsonify({"status" : 200, 
                    "data" : [{
                        "id" : id,
                        "message" : "red-flag record has been deleted for id {}".format(id)
                        }]
                    })
    return helper.error_404_message(id)

#------------------------------------------------------------------------------------------

#Start Server------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
    
    