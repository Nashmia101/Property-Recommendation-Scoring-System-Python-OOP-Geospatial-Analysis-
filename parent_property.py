# Copy and paste your class from the previous function
from abc import ABC, abstractmethod
from typing import Tuple, List, Union
from amenity import Amenity

class Property(ABC):
    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        floor_area: int,
                        price: int,
                        property_features: List[str],
                        coordinates: Tuple[float, float]):
        self.prop_id = prop_id 
        self.bedrooms = bedrooms 
        self.bathrooms = bathrooms 
        self.parking_spaces = parking_spaces 
        self.full_address = full_address 
        self.floor_area = floor_area 
        self.price = price 
        self.property_features = property_features 
        self.coordinates = coordinates 
                               
        #raise NotImplementedError

    def get_prop_id(self) -> str:
        return self.prop_id
        #raise NotImplementedError

    def get_full_address(self) -> str:
        return self.full_address
        
        #raise NotImplementedError

    def get_suburb(self) -> str:
        address_list= self.full_address.split(" ")
        suburb_data = address_list[3]
        self.subrub = suburb_data
        return self.subrub
        #raise NotImplementedError
    
    def get_prop_type(self) -> str:
        return self.prop_type
        #raise NotImplementedError
    
    def set_bedrooms(self, bedrooms: int) -> None:
        self.bedrooms = bedrooms
        #raise NotImplementedError
    
    def get_bedrooms(self) -> int:
        return self.bedrooms
        #raise NotImplementedError
    
    def set_bathrooms(self, bathrooms: int) -> None:
        self.bathrooms = bathrooms
        #raise NotImplementedError
    
    def get_bathrooms(self) -> int:
        return self.bathrooms
    
    def set_parking_spaces(self, parking_spaces: int) -> None:
        self.parking_spaces = parking_spaces
        #raise NotImplementedError

    def get_parking_spaces(self) -> int:
        return self.parking_spaces
        #raise NotImplementedError
    
    def get_coordinates(self) -> Tuple[float, float]:
        return self.coordinates
        #raise NotImplementedError
    
    def set_floor_number(self, floor_number: int) -> None:
        self.floor_number=floor_number
        #raise NotImplementedError

    def get_floor_number(self) -> Union[int,None]:
        return self.floor_number  
        #raise NotImplementedError
    
    def set_land_area(self, land_area: int) -> None:
        self.land_area=land_area
        #raise NotImplementedError

    def get_land_area(self) -> Union[int,None]:
        return self.land_area  
        #raise NotImplementedError
    
    def set_floor_area(self, floor_area: int) -> None:
        self.floor_area=floor_area
        #raise NotImplementedError
    
    def get_floor_area(self) -> int:
        return self.floor_area                          
        #raise NotImplementedError

    def set_price(self, price: int) -> None:
        self.price = price
        #raise NotImplementedError
    
    def get_price(self) -> int:
        return self.price
        #raise NotImplementedError
    
    def set_property_features(self, property_features: List[str]) -> None:
        self.property_features = property_features
        #raise NotImplementedError
    
    def get_property_features(self) -> List[str]:
        return self.property_features
        #raise NotImplementedError

    def add_feature(self, feature: str) -> None:
        prop_feat_lst = list(self.property_features)
        if feature in prop_feat_lst:
            pass
        else:
            prop_feat_lst.append(feature)
            self.property_features = prop_feat_lst

    def remove_feature(self, feature: str) -> None:
        prop_feat_lst = list(self.property_features)
        if feature in prop_feat_lst:
            prop_feat_lst.remove(feature)
            self.property_features = prop_feat_lst
        else:
            pass

   
    def __haversine_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        import math

        # Convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        radius_of_earth = 6371  # Radius of the earth in kilometers.
        distance = radius_of_earth * c

        return distance

    def nearest_amenity(self, amenities: List[Amenity], amenity_type: str, amenity_subtype: str = None) -> Tuple[Amenity, float]:
        min_distances = []
        closest_amenities = []

        for amenity in amenities:
            if amenity.get_amenity_type() == amenity_type:
                if amenity_subtype is None or amenity.get_amenity_subtype() == amenity_subtype:
                    distance = self.__haversine_distance(self.coordinates[0], self.coordinates[1], amenity.get_amenity_coords()[0], amenity.get_amenity_coords()[1])
                    
                    min_distances.append(distance)
                    closest_amenities.append(amenity)
                elif amenity_subtype == 'Primary' and amenity.get_amenity_subtype() in ['Pri/Sec', 'Primary']:
                    distance = self.__haversine_distance(self.coordinates[0], self.coordinates[1], amenity.get_amenity_coords()[0], amenity.get_amenity_coords()[1])
                    
                    min_distances.append(distance)
                    closest_amenities.append(amenity)
                elif amenity_subtype == 'Secondary' and amenity.get_amenity_subtype() in ['Pri/Sec', 'Secondary']:
                    distance = self.__haversine_distance(self.coordinates[0], self.coordinates[1], amenity.get_amenity_coords()[0], amenity.get_amenity_coords()[1])
                    
                    min_distances.append(distance)
                    closest_amenities.append(amenity)
                elif amenity_subtype == 'Pri/Sec' and amenity.get_amenity_subtype() in ['Pri/Sec', 'Primary', 'Secondary']:
                    distance = self.__haversine_distance(self.coordinates[0], self.coordinates[1], amenity.get_amenity_coords()[0], amenity.get_amenity_coords()[1])
                    
                    min_distances.append(distance)
                    closest_amenities.append(amenity)

        min_distance_index = min_distances.index(min(min_distances))       
        closest_amenity = closest_amenities[min_distance_index]
        min_distance = min_distances[min_distance_index]

        return closest_amenity, min_distance
if __name__ == '__main__':
    pass
