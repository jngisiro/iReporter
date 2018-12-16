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
    assert response.status_code == 201
    assert response.content_type == "application/json" 
    assert response.get_json()["status"] == response.status_code                         
    assert response.get_json()["data"][0]["message"][:-2] == "Created red-flag record for id"

def test_created_incident():
    """ Run tests to confirm the incident was created and follows the data rules """
    response = TEST_CLIENT.get("/api/v1/red_flags/4/")
    assert response.status_code == 200
    assert response.content_type == "application/json" 
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
    assert response.get_json()["status"] == response.status_code
    assert len(response.get_json()["data"]) == len(incident.helper.RED_FLAGS)
    assert response.get_json()["data"][0]["title"] == incident.helper.RED_FLAGS[0]["title"]

def test_get_specific_incident():
    response = TEST_CLIENT.get("/api/v1/red_flags/1/")
    assert response.status_code == 200
    assert len(response.get_json()["data"]) == len(incident.helper.RED_FLAGS[0])
    assert response.get_json()["data"]["title"] == incident.helper.RED_FLAGS[0]["title"]

def test_get_incident_with_invalid_id():
    response = TEST_CLIENT.get("/api/v1/red_flags/5/")
    assert response.status_code == 404
    assert response.get_json()["status"] == response.status_code
    assert response.get_json()["error"] == "No record found for red-flag with id 5"

def test_edit_incident(id = 2):
    response = TEST_CLIENT.patch("/api/v1/red_flags/2/", 
                    content_type = "application/json",
                    data = json.dumps({  
                        "title" : "Theft a UNRA Kyambogo",
                        "images" : "corrupt.jpg",
                        "videos" : "corrupt.mp4",
                        "comment" : "Altered the red flag comment"
                    }))
    assert response.status_code == 201
    assert response.get_json()["status"] == response.status_code
    assert response.get_json()["data"][0]["id"] == id
    assert response.get_json()["data"][0]["message"] == f"Updated red-flag record for id {id}"
    

def test_editted_incident():
    """ Run tests to confirm the incident was editted """
    response = TEST_CLIENT.get("/api/v1/red_flags/2/")
    assert response.get_json()["data"]["title"] == "Theft a UNRA Kyambogo"
    assert response.get_json()["data"]["images"] == "corrupt.jpg"
    assert response.get_json()["data"]["videos"] == "corrupt.mp4"
    assert response.get_json()["data"]["comment"] == "Altered the red flag comment" 

def test_edit_incident_with_invalid_id(id=10):
    response = TEST_CLIENT.patch(f"/api/v1/red_flags/{id}/", 
                    content_type = "application/json",
                    data = json.dumps({  
                        "title" : "Theft a UNRA Kyambogo",
                        "images" : "corrupt.jpg",
                        "videos" : "corrupt.mp4",
                        "comment" : "Altered the red flag comment"
                    }))
    assert response.status_code == 404
    assert response.get_json()["status"] == response.status_code
    assert response.get_json()["error"] == f"No record found for red-flag with id {id}"


def test_delete_incident():
    response = TEST_CLIENT.delete("/api/v1/red_flags/1/")
    assert response.status_code == 200
    assert response.get_json()["data"][0]["message"] == "red-flag record has been deleted for id 1"

def test_deleted_incident():
    """ Run test to confirm the incident has been deleted """
    response = TEST_CLIENT.delete("/api/v1/red_flags/1/")
    assert response.status_code == 404
    assert response.get_json()["status"] == 404
    assert response.get_json()["error"] == "No record found for red-flag with id 1"