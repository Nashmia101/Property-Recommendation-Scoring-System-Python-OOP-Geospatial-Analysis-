def extract_information(property_string: str) -> dict:
    header1_string = "prop_id,full_address,bedrooms,bathrooms,parking_spaces,latitude,longitude,floor_number,land_area,floor_area,price,property_features"
    header_string = header1_string.split(",")
    header_string.insert(1,"prop_type")
    header_string.insert(3,"suburb")
    dic = {}
    property_string = property_string.split(",")
    property_string.insert(1,"")
    property_string.insert(3,"")
    #print(len(property_string))
    if property_string[9] == "":
        del property_string[9]
        del header_string[9]
        property_string[1] = "house"
    if property_string[10] == "":
        del property_string[10]
        del header_string[10]  
        property_string[1] = "apartment" 
    if property_string[12]== '':
        property_string[12] = [] 
    else:
        property_string[12]= property_string[12].split(";")
        property_string[12] = [feature.strip() for feature in property_string[12]]


    address_list= property_string[2].split(" ")
    suburb_data = address_list[3]
    property_string[3] = suburb_data
    #print(suburb_data)

    for i in range(4,7):
        property_string[i]= int(property_string[i])
    for i in range(7,9):
        property_string[i]= float(property_string[i])
    for i in range(9,12):
        property_string[i]= int(property_string[i])

    for h in range(len(header_string)):
            dic[header_string[h]] = property_string[h]   
    #print(dic)
    return dic
    #raise NotImplementedError

def add_feature(property_dict: dict, feature: str) -> None:
    property_features_list = list(property_dict['property_features'])
    if feature in property_features_list:
        pass
    else:
        property_features_list.append(feature)
    property_dict['property_features']= property_features_list
    #raise NotImplementedError

def remove_feature(property_dict: dict, feature: str) -> None:
    property_features_list = list(property_dict['property_features'])
    if feature in property_features_list:
        property_features_list.remove(feature)
    else:
        pass
    property_dict['property_features']= property_features_list
    #raise NotImplementedError

def main():
    sample_string ="P10001,3 Antrim Place Langwarrin VIC 3910,4,2,2,-38.16655678,145.1838435,,608,257,870000,dishwasher;central heating"
    property_dict = extract_information(sample_string)
    print(f"The first property is at {property_dict['full_address']} and is valued at ${property_dict['price']}")

    sample_string_2 ="P10002,G01/7 Rugby Road Hughesdale VIC 3166,2,1,1,-37.89342337,145.0862616,1,,125,645000,dishwasher;air conditioning;balcony"
    property_dict_2 = extract_information(sample_string_2)

    print(f"The second property is in {property_dict_2['suburb']} and is located on floor {property_dict_2['floor_number']}")

    add_feature(property_dict, 'electric hot water')
    print(f"Property {property_dict['prop_id']} has the following features: {property_dict['property_features']}")
    
   
if __name__ == '__main__':
    main()
