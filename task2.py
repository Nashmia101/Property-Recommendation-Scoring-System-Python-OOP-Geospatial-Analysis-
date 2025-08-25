# DO NOT DELETE THIS LINE
from haversine import haversine_distance

def process_properties(file_name: str) -> dict:
    """
    Processes a CSV file containing property data and formats it into a structured dictionary.
    
    Args:
        file_name: A string representing the file path of the properties CSV file. (The name of the CSV file to process.)
    
    Returns:
        A dictionary with property IDs as keys and corresponding property details as values.
    """
    # Initialize an empty dictionary to hold the properties.
    outer_dict = {}
    # Read the properties CSV file.
    with open(file_name, "r") as fileref:
        lines = fileref.readlines()

        # Define the header for the property attributes
        header1_string = lines[0]
        # Split the header string into a list of attributes to form the keys for the dictionary
        header_string = header1_string.strip().split(",")
        # Adding the prop_type and suburb to the header_string
        # Insert 'prop_type' into the header list at position 1
        header_string.insert(1, "prop_type")
        # Insert 'suburb' into the header list at position 3
        header_string.insert(3, "suburb")

        for line in lines[1:]:
            # Initialize an empty dictionary to hold the properties' data
            inner_dict = {}
            # Split the input property string into a list of values corresponding to the attributes in the header
            property_string = line.strip().split(",")
            # Insert empty strings at positions 1 and 3 where 'prop_type' and 'suburb' will be added later
            property_string.insert(1, "")
            property_string.insert(3, "")

            # Determine property type based on CSV columns
            #Determine if the property is an apartment or a house based on the address format
            address_prop_type = property_string[2].split(' ')[0]
            if "/" in address_prop_type:
                # Set the property type at index 1 to 'apartment'
                property_string[1] = 'apartment'
            else:
                # Set the property type at index 1 to 'house'
                property_string[1] = 'house'

            # Convert features string into a list, or set to empty if missing                
            if property_string[13]=="":
                property_string[13] = []
            else:
                property_string[13] = property_string[13].split(";")
                property_string[13] = [feature.strip() for feature in property_string[13]]
                
            # Extract suburb name from address
            address_list = property_string[2].split(" ")
            suburb_data = address_list[3]
            # Update the property string at index 3 with the extracted suburb name
            property_string[3] = suburb_data

            # Convert appropriate fields to integers or floats
            for i in range(4, 7):
                if len(property_string) > i and property_string[i]:
                    property_string[i] = int(property_string[i])

            for i in range(7, 9):
                if len(property_string) > i and property_string[i]:
                    property_string[i] = float(property_string[i])

            for i in range(9, 13):
                if len(property_string) > i and property_string[i]:
                    property_string[i] = int(property_string[i])

            # Create the dictionary of property details
            for h in range(len(header_string)):
                # Check if the current index (h) is less than the length of property_string to avoid out of range errors
                if h < len(property_string):
                    # Assign the value from property_string at index h to the corresponding header in inner_dict
                    inner_dict[header_string[h]] = property_string[h]

            # Use the first item in property_string as a unique key and assign the inner_dict as its value in outer_dict        
            outer_dict[property_string[0]] = inner_dict

            # Remove empty or unnecessary fields
            for prop_id, prop_info in list(outer_dict.items()):
                if 'floor_number' in prop_info and prop_info['floor_number'] == '':
                    # Remove the 'floor_number' key from the dictionary
                    outer_dict[prop_id].pop('floor_number', None)
                if 'land_area' in prop_info and prop_info['land_area'] == '':
                    # Remove the 'land_area' key from the dictionary
                    outer_dict[prop_id].pop('land_area', None)
    print(outer_dict)                
    return outer_dict

def process_stations(file_name: str) -> dict:
    """
    Processes a CSV file containing train station data and formats it into a structured dictionary.
    
    Args:
        file_name: A string representing the file path of the train stations CSV file.
    
    Returns:
        A dictionary with station IDs as keys and corresponding station details as values.
    """
    # Initialize an empty dictionary to store the outer layer of station data
    outer_dict1 = {}
    # Open the specified file in read mode
    with open(file_name, "r") as fileref1:
        lines1 = fileref1.readlines()
        # Extract the header line and split it into components based on commas
        header1_string1 = lines1[0]
        header_string2 = header1_string1.strip().split(",")

        # Process each line in the file starting from the second line (skipping the header)
        for line in lines1[1:]:
            # Initialize an empty dictionary for storing inner layer of station data
            inner_dict1 = {}
            train_string = line.strip().split(",")
            # Convert specific fields (indices 2 and 3) from string to float
            for i in range(2, 4):
                    train_string[i] = float(train_string[i])
            # Map each element of the line to its corresponding header
            for h in range(len(header_string2)):
                 if h < len(train_string):
                    # Ensure there are no index out of range errors
                    inner_dict1[header_string2[h]] = train_string[h]

            # Use the first element of train_string as a unique key for the outer dictionary
            outer_dict1[train_string[0]] = inner_dict1  
                
    return outer_dict1

def nearest_station(properties: dict, stations: dict, prop_id: str) -> str:
    """
    Determines the nearest train station to a given property using the haversine formula.
    
    Args:
        properties: A dictionary containing property details including coordinates.
        stations: A dictionary containing station details including coordinates.
        prop_id: The property ID for which the nearest station is to be found.
    
    Returns:
        The name of the nearest train station to the specified property.
    """
    # Retrieve property information by property ID from the properties dictionary
    prop_info = properties.get(prop_id) 
    # Retrieve latitude and longitude of the property
    lat1 = prop_info.get('latitude')  # Retrieve latitude of the property
    lon1 = prop_info.get('longitude') # Retrieve longitude of the property

    # Initialize an empty list to store distances between the property and each station
    dist_list = []

    # Get a list of station ID's
    inner_stations = list(stations.keys())
    # Loop through each station to calculate the distance from the property
    for station in range(len(inner_stations)):
        # Extract all values (attributes) of the current station
        station_keys = list(stations[inner_stations[station]].values())
        # Retrieve latitude and longitude of the station
        lat2 = station_keys[2]
        lon2 = station_keys[3]
        # Calculate the haversine distance between the property and the station
        num= haversine_distance(lat1, lon1, lat2, lon2)
        # Append the calculated distance to the list
        dist_list.append(num)   

    # Find the minimum distance from the dist_list to determine the nearest station
    closest_dist = min(dist_list)
    # Find the index of the closest distance in the list
    identity = dist_list.index(closest_dist)
    # Convert the index to string to use as a key to find the station in the stations dictionary
    identity2 = str(inner_stations[identity])
    # Retrieve the name of the nearest station using the station identifier
    nearest_station = stations[identity2]["stop_name"]
    
    return nearest_station    

def main():
    """
    You need not touch this function, if your 
    code is correct, this function will work as intended 
    """
    # Process the properties
    properties_file = 'sample_properties.csv'
    properties = process_properties(properties_file)

    # Process the train stations
    stations_file = 'train_stations.csv'
    stations = process_stations(stations_file)

    # Check the validity of stations
    sample_prop = 'P10005'
    print(f"The nearest station for property {sample_prop} is {nearest_station(properties, stations, sample_prop)}")
    


if __name__ == '__main__':
    main()
