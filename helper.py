from datetime import datetime
from flask import request
#Set Date format to be used--------------------------------------------------------------
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

#Status Codes --------------------------------------------------------------------------
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

#Get request json content ----------------------------------------------------------------------------------------
def get_request_json():
    if request.content_type == "application/json":
        return request.get_json()
    else:
        return request.form.to_dict()
