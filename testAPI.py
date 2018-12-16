from flask import jsonify
import unittest
import incident
import json
import sys

TEST_CLIENT = incident.app.test_client()
test_data = {
                        "title" : "Theft at UNRA Banda",
                        "createdBy" : 5,
                        "type" : "red-flag",
                        "location" : "LAT234, LOG342",
                        "status" : "draft",
                        "images" : ["img/image1.jpg", "img/image2.jpg"],
                        "videos" : ["vid/video1.mp4", "vid/video2.jpg"],
                        "comment" : "It is a long established fact that a reader will be distracted by the readable content of a page"
                                }
    
def test_create_incident():
    """ Add a new red-flag """
    response = TEST_CLIENT.post("/api/v1/red_flags/",
                    data = json.dumps(test_data), content_type="application/json")                      
    assert response.get_json()["data"][0]["message"][:-2] == "Created red-flag record with id"
    assert response.content_type == "application/json"

def test_created_incident():
    """ Run tests to confirm the incident was created and follows the data rules """
    response = TEST_CLIENT.get("/api/v1/red_flags/4/")
    assert response.get_json()["data"]["title"] == test_data["title"]
    assert response.get_json()["data"]["createdBy"] == test_data["createdBy"]
    assert response.get_json()["data"]["location"] == test_data["location"]
    assert response.get_json()["data"]["status"] == test_data["status"]
    assert response.get_json()["data"]["images"] == test_data["images"]
    assert response.get_json()["data"]["videos"] == test_data["videos"]
    assert response.get_json()["data"]["comment"] == test_data["comment"]
  
    

def test_get_all_incidents():
    response = TEST_CLIENT.get("/api/v1/red_flags/")
    assert response.status_code == 200
    assert len(response.get_json()["data"]) == len(incident.RED_FLAGS)
    assert response.get_json()["data"][0]["title"] == incident.RED_FLAGS[0]["title"]

def test_get_specific_incident():
    response = TEST_CLIENT.get("/api/v1/red_flags/1/")
    assert response.status_code == 200
    assert len(response.get_json()["data"]) == len(incident.RED_FLAGS[0])
    assert response.get_json()["data"]["title"] == incident.RED_FLAGS[0]["title"]

def test_edit_incident():
    response = TEST_CLIENT.patch("/api/v1/red_flags/2/", 
                    content_type = "application/json",
                    data = json.dumps({  
                        "title" : "Theft a UNRA Kyambogo",
                        "images" : "corrupt.jpg",
                        "videos" : "corrupt.mp4",
                        "comment" : "Altered the red flag comment"
                    }))
    assert response.status_code == 200

def test_delete_incident():
    response = TEST_CLIENT.delete("/api/v1/red_flags/1/")
    assert response.status_code == 200
    assert response.get_json()["data"][0]["message"] == "red-flag record has been deleted for id 1"