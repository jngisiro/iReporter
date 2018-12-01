user = {}   #Instantiate a new user with key:value pairs
users = [{"id": 0, "firstname" : "Museveni", "lastname" : "Yoweri",
                "othernames" : "Kaguta", "email":"ymuseveni@gmail.com", 
                "phonenumber":"0772340340", "username": "ykm7",
                "registered": datetime(), "isadmin": False }]  #Store collection of red flags

#Add New Red Flag -------------------------------------------------------------------------
@app.route("/users", methods=["POST"])
def add_new_user():
    """ Should return Status Code:201 if a User is created"""
    user["id"] = len(users)
    user["firstname"] = request.form["firstname"]
    user["lastname"] = request.form["lastname"]
    user["othernames"] = request.form["othernames"]
    user["email"] = request.form["email"]
    user["phonenumber"] = request.form["phonenumber"]
    user["username"] = request.form["username"]
    user["isadmin"] = False
    user["registered"] = datetime()
    users.append(red_flag)
    return jsonify({"Status" : 201, "Message" : Created})

#Get all Users ------------------------------------------------------------------------
@app.route("/users", methods=["GET"])
def get_all_users():
    """ Should return Status Code:200 along with all the Red Flags |
        Code:404 if there are no Red Flags
    """
    return jsonify({"Status" : 200, "Message" : users})     # unpack dictionary

#Get specific User by id ---------------------------------------------------------------
@app.route("/users/<string:id>/", methods=["GET"])
def get_user_by(id):
    """ Should return Status Code:200 along with the requested Users |
        Code:404 if there is no User for the specified id
    """
    if int(id) > len(users):
        return jsonify({"Status" : 404, "Message" : "Not Found"}) #red_flags[id]
    return jsonify({"Status" : 200, "Message" : users[int(id)] }) #red_flags[id]

#Edit Specific User ------------------------------------------------------------------
@app.route("/users/<string:id>", methods=["PUT"])
def edit_user_by(id):
    """ Should return Status Code:200 along with the requested Red Flag |
        Code:404 if there is no User for the specified id
    """
    user["firstname"] = request.form["firstname"]
    user["lastname"] = request.form["lastname"]
    user["othernames"] = request.form["othernames"]
    user["email"] = request.form["email"]
    user["phonenumber"] = request.form["phonenumber"]
    user["username"] = request.form["username"]
    return jsonify({"Status" : 200, "Method" : "Updated"})

#Delete User ----------------------------------------------------------------
@app.route("/users/<string:id>", methods=["DELETE"])
def delete_user_by(id):
    """ Should return Status Code:200 if User is deleted |
        Code:404 if there is no User for the specified id
    """
    del users[id]
    return jsonify({"Status" : 200, "Message" : "Deleted"})

#------------------------------------------------------------------------------------------
#Start Server------------------------------------------------------------------------------
