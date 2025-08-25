import os
import json
from typing import List, Tuple, Dict
from parent_property import Property
from child_properties import House, Apartment
from amenity import Amenity
from ingestion import ingest_files
from score import *

def read_request(request_filename: str) -> Tuple[dict, dict]:
    """
    This method reads a request file in json format
    and returns two dictionaries; one containing the
    house_importance features and one containing the 
    amenity_importance features.
    """
    # TODO: Step 1 - Define this method to read a JSON request and return 2 dictionaries
    with open(request_filename, "r") as file:
        data = json.load(file)
        request_data = data.get("request", {})
        #print(data)
        if "house_importance" in request_data:
            house=request_data["house_importance"]
            
        if "amenities_accessibility" in request_data:
            amenity=request_data["amenities_accessibility"]
    
    #return house_importance,amenities_accessibility
    return house, amenity     

    #raise NotImplementedError

def find_matching_properties(props: List[Property], house_importance: dict) -> List[Property]:
    """
    THis method recevied a list of all properties and a dictionary that
    contains the house importance criteria from a user's request 
    and returns a list of Property objects that match the user's request
    """
    # TODO: Step 2 - Define this method to return a list of matching properties
    #raise NotImplementedError
    matching_properties = []
    
    for prop in props:
        # Check property type and suburb for full match
        if 'prop_type' in house_importance and prop.get_prop_type() != house_importance['prop_type']:
            continue

        if 'suburb' in house_importance and prop.get_suburb() != house_importance['suburb']:
            continue

        # Check for feature full match
        #if 'property_features' in house_importance and any(feature in prop.get_property_features() for feature in house_importance['property_features']):
        #    continue
        if 'property_features' in house_importance and house_importance['property_features'] not in prop.get_property_features():
            continue    
        # Check for baseline or ceiling values
        if 'floor_area' in house_importance and prop.get_floor_area() < house_importance['floor_area']:
            continue
        if 'land_area' in house_importance and prop.get_land_area() < house_importance['land_area']:
            continue
        if 'bedrooms' in house_importance and prop.get_bedrooms() < house_importance['bedrooms']:
            continue
        if 'bathrooms' in house_importance and prop.get_bathrooms() < house_importance['bathrooms']:
            continue
        if 'parking_spaces' in house_importance and prop.get_parking_spaces() < house_importance['parking_spaces']:
            continue
        if 'floor_number' in house_importance and prop.get_floor_number() > house_importance['floor_number']:
            continue
        if 'price' in house_importance and prop.get_price() > house_importance['price']:
            continue

        # If all checks pass, add to matching properties
        matching_properties.append(prop)
        #print(prop.get_prop_id(),prop.get_property_features())
        
    return matching_properties 
    
def create_response_dict(scored_properties: dict) -> dict:
    """
    This method takes in a dictionary that has the property objects 
    and their star scores and creates a dictionary in JSON format 
    that can be written into a file
    """
    response_dict = {"properties": []}

    for star_score, property_obj in scored_properties.items():
        property_id = property_obj.get_prop_id()
        star_score_float = float(star_score)
        property_info = {"property_id": property_id}
        property_info["star_score"] = star_score_float
        response_dict["properties"].append(property_info)
    #print(response_dict)
    return response_dict

def produce_star_scores(request_filename: str, properties_file: str, amenities_files: List[str]) -> dict:
    # Read the properties and amenities
    medical_file, schools_file, train_stations, sport_facilities = amenities_files
    props, amenities = ingest_files(properties_file, medical_file, schools_file, train_stations, sport_facilities)

    # Read the request and get the dictionaries of house_importance and amenity_accessibility
    house_importance, amenity_accessibility = read_request(request_filename)

    # Collect properties that match the property criteria
    matched_props = find_matching_properties(props, house_importance)

    # Score properties using the amenity amenity_accessibility dictionary
    prop_scores = [score_property(x, amenities, amenity_accessibility) for x in matched_props]

    # Now, we can normalise the scores that we just got
    norm_scores = normalise_scores(prop_scores)

    # Create a collection matching property object to Score
    prop_scored = dict(zip(norm_scores, matched_props))

    # Create a response dictionary
    response_dict = create_response_dict(prop_scored)
    #print(response_dict)
    
    # Return the response dictionary from step 3 and the list of matching property family objects
    return response_dict, matched_props

def sort_properties(property_info):
    # Sort by star score (descending) and property ID (ascending)
    return (-property_info["star_score"], property_info["property_id"])

def respond(response_dict: dict) -> None:
    """
    This function reads a response dictionary and creates a JSON 
    file based on the content of the response dictionary
    """
    sorted_properties = sorted(response_dict["properties"], key=sort_properties)

    # Create the response JSON structure
    response_data = {"properties": sorted_properties}

    # Write the response JSON to a file
    with open("response1.json", "w") as file:
        json.dump(response_data, file, indent=4)

    # TODO: Step 4 - Create this method to read a response dictionary
    # and create a JSON file
   
if __name__ == '__main__':
    response_dict, matched_props = produce_star_scores('request.json', 'melbourne_properties.csv', ['melbourne_medical.csv', 'melbourne_schools.csv', 'train_stations.csv', 'sport_facilities.csv'])
    print(f"{len(matched_props)} properties matched with the user's request")
    respond(response_dict)
    # Check if response.json exists in the current directory
    if os.path.exists("/home/response.json"):
        print("File created successfully")
    else:
        print("File not created. Some Error occurred")
