import pandas as pd
import numpy as np
import json, requests
import os
from dotenv import load_dotenv
load_dotenv()
import requests



def transformToGeoPoint(s):
    
    if np.isnan(s.latitude) or np.isnan(s.longitude):
        
        return None
    
    return {
        "type":"Point",
        "coordinates":[s.longitude, s.latitude]
    }


def geoQueryNear(point,radius):
    return {
        "geopoint":{
            "$near": {
                "$geometry": point,
                "$maxDistance": radius,
                "$minDistance": 0
            }
        }
    }