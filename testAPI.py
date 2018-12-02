from flask import jsonify
import unittest
import incident
import json
import sys

TEST_CLIENT = incident.app.test_client()

    
# def test_create_incident(self):
#     """ Add a new red-flag """
#     response = self.app.post("/red_flags/", 
#                     content_type = "application/json",
#                     data = jsonify({
#                         "title" : "Theft at UNRA Banda",
#                         "createdBy" : 5,
#                         "type" : "red-flag",
#                         "location" : "LAT234, LOG342",
#                         "status" : "draft",
#                         "Images" : ["img/image1.jpg", "img/image2.jpg"],
#                         "Videos" : ["vid/video1.mp4", "vid/video2.jpg"],
#                         "comment" : "It is a long established fact that a reader will be distracted by the readable content of a page"
#                                 }))
#     assert response.status_code == 200

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

# def test_edit_incident(self):
#     response = self.app.patch("/red_flags/", 
#                     content_type = "application/json",
#                     data = jsonify({
#                         "title" : "Theft a UNRA Kyambogo",
#                         "image" : "corrupt.jpg",
#                         "video" : "corrupt.mp4"
#                     }))
    #assert response.status_code == 200

def test_delete_incident():
    response = TEST_CLIENT.delete("/api/v1/red_flags/1/")
    assert response.status_code == 200