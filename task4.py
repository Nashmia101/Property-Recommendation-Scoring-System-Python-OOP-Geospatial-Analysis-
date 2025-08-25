from ingestion import ingest_files

if __name__ == '__main__':
    props, amens = ingest_files('sample_properties.csv', 'sample_melbourne_medical.csv', 'sample_melbourne_schools.csv', 'train_stations.csv', 'sample_sport_facilities.csv')
    print(f"Read {len(props)} properties and {len(amens)} amenities")
    print(f"First property at {props[9].get_full_address()} is valued at ${props[9].get_price()}")

    counts = {'train_station': 0, 'medical_centre': 0, 'school': 0, 'sport_facility': 0}
    for amenity in amens:
        counts[amenity.get_amenity_type()] += 1
        print(amenity.get_amenity_type())
        print(amenity.get_amenity_subtype())    
    print("Here are the counts for the amenities read")
    for k,v in counts.items():
        print(k,":",v)
