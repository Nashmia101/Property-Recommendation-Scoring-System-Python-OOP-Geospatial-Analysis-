import csv, json
def process_schools(file_name: str) -> dict:
    """
    Processes a CSV file containing school data and formats it into a structured dictionary.
    Args:
        file_name: A string representing the file path of the sample_melbourne_schools CSV file.
    Returns:
        A dictionary with school_no as keys and corresponding school details as values.
    """
    # Initialize an empty dictionary to hold the schools.
    outer_dict_school= {}
    # Read the schools CSV file.
    with open(file_name, "r", encoding='utf-8-sig') as file_school:
        csv_reader_school = csv.DictReader(file_school)
        # Loop for reading every row of schools
        for row_school in csv_reader_school:

            inner_dict_school = {} # Creaing inner dictionary 
            school_lat_str = row_school['school_lat'] # extracting latitude
            school_lon_str =row_school['school_lon'] # extracting longitude

            if school_lon_str == 'NA' or not school_lon_str:
                continue  # Ignore rows with empty or 'NA' location
            if school_lat_str == 'NA' or not school_lat_str:
                continue  # Ignore rows with empty or 'NA' location
            inner_dict_school=row_school.copy() # Create a copy of the row to avoid modifying the original row
            # assigning every row with school details, with school no as key to the outer dictionary 
            outer_dict_school[row_school['school_no']] = inner_dict_school
            # converting lat and lon values to float
            inner_dict_school['school_lat'] = float(inner_dict_school['school_lat'])
            inner_dict_school['school_lon'] = float(inner_dict_school['school_lon'])
            # removing unnecessary items that are not needed in the final dictionary 
            unnecessary_items = list(inner_dict_school.keys())
            unnecessary_items = unnecessary_items[3:17]
            for school_no, school_info in list(outer_dict_school.items()):
                for not_ in unnecessary_items:
                    if not_ in school_info:
                        outer_dict_school[school_no].pop(not_, None)                        
    # Returning school final dictionary
    return outer_dict_school


def process_medicals(file_name: str) -> dict:
    """
    Processes a CSV file containing medical facilities data and formats it into a structured dictionary.
    
    Args:
        file_name: A string representing the file path of the sample_melbourne_medical CSV file.
    
    Returns:
        A dictionary with gp_code as keys and corresponding medical facilities details as values.
    """
    # Initialize an empty dictionary to hold the medical facilities.
    outer_dict_medical = {}
    # Read the medical CSV file.
    with open(file_name, "r", encoding='utf-8-sig') as file_med:
        csv_reader_medical = csv.DictReader(file_med)
        # Loop for reading every row of medical facilities
        for row_medical in csv_reader_medical:
            
            inner_dict_medical = {}  # creaing inner dictionary
            location_str = row_medical['location']  # extracting location
            if location_str == 'NA' or not location_str:
                continue  # Ignore rows with empty or 'NA' location
            try: # Using json module to process the inner dictionary that has longitude and latitude
                data_medical = json.loads(location_str)
                if 'lat' not in data_medical or 'lng' not in data_medical:
                    continue  # Skip rows with missing latitude or longitude
                # Storing python dictionary into location index
                row_medical['location'] = data_medical
                inner_dict_medical=row_medical.copy() # Create a copy of the row to avoid modifying the original row
                # assigning every row with medical facilities details with gp_code as key to the outer dictionary 
                outer_dict_medical[row_medical['gp_code']] = inner_dict_medical
                # converting longitude and latitude into float
                medical_lat = float(inner_dict_medical["location"]['lat'])
                medical_lon = float(inner_dict_medical["location"]['lng'])
                # storing mediacl_lat and medical_lon as values to keys gp_lat and gp_lon
                inner_dict_medical['gp_lat']=medical_lat
                inner_dict_medical['gp_lon']=medical_lon
                # removing location key 
                del inner_dict_medical["location"]

            except json.JSONDecodeError:
                continue  # Ignore rows with invalid JSON in location
            # removing address and phone items from the final dictionary since we do not need them according to the instructions
            for med_no, med_info in list(outer_dict_medical.items()):
                if "Address" in med_info:
                    outer_dict_medical[med_no].pop("Address", None)
                if "Phone" in med_info:
                    outer_dict_medical[med_no].pop("Phone", None)
            
    # returning the final medical dictionary 
    return outer_dict_medical

def process_sport(file_name: str) -> dict:
    """
    Processes a CSV file containing sport facility data and formats it into a structured dictionary.
    
    Args:
        file_name: A string representing the file path of the sample_sport_facilities CSV file.
    
    Returns:
        A dictionary with facility_id as keys and corresponding sport facilities details as values.
    """
    # Initialize an empty dictionary to hold the sport facilities.
    outer_dict_sports= {}
    # Read the sports CSV file.
    with open(file_name, "r", encoding='utf-8-sig') as file_sports:
        csv_reader_sports = csv.DictReader(file_sports)
         #loop for reading every row of sport facilities
        for row_sports in csv_reader_sports:

            inner_dict_sports = {} # creaing inner dictionary 
            sport_lat_str = row_sports['sport_lat'] #extracting latitude
            sport_lon_str = row_sports['sport_lon'] #extracting longitude

            if sport_lat_str == 'NA' or not sport_lat_str:
                continue  # Ignore rows with empty or 'NA' location
            if sport_lon_str == 'NA' or not sport_lon_str:
                continue  # Ignore rows with empty or 'NA' location
            inner_dict_sports=row_sports.copy() # Create a copy of the row to avoid modifying the original row
            
            # assigning every row with sport facilities details with facility id as key to the outer dictionary 
            outer_dict_sports[row_sports['facility_id']] = inner_dict_sports
            # converting longitude and latitude into float
            inner_dict_sports['sport_lat'] = float(inner_dict_sports['sport_lat'])
            inner_dict_sports['sport_lon'] = float(inner_dict_sports['sport_lon'])

             # removing unnecessary items that are not needed in the final dictionary from the dictionary
            unnecessary_items_sports = list(inner_dict_sports.keys())
            unnecessary_items_sports = unnecessary_items_sports[1:2]
            for sport_no, sport_info in list(outer_dict_sports.items()):
                for not_sports in unnecessary_items_sports:
                    if not_sports in sport_info:
                        outer_dict_sports[sport_no].pop(not_sports, None)      

    #returning sport final dictionary
    return outer_dict_sports

def main():
    school_dict = process_schools('sample_melbourne_schools.csv')
    medical_dict = process_medicals('sample_melbourne_medical.csv')
    sport_dict = process_sport('sample_sport_facilities.csv')

    sample_medical_code = 'mgp0041'
    print(f"There are {len(school_dict)} schools and {len(sport_dict)} sport facilities in our dataset")
    print(f"The location for {medical_dict[sample_medical_code]['gp_name']} is {medical_dict[sample_medical_code]['gp_lat']}, {medical_dict[sample_medical_code]['gp_lon']}")

if __name__ == '__main__':
    main()

