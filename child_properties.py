# Copy and paste your code from the previous task
from typing import Tuple, List, Union
from parent_property import Property

class House(Property):
    #prop_type="House"
    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        land_area: int,
                        floor_area: int,
                        price: int,
                        property_features: List[str],
                        coordinates: Tuple[float, float]):

        super().__init__(prop_id,bedrooms,bathrooms,parking_spaces,full_address,floor_area,price,property_features,coordinates)  
        self.land_area=land_area 
        self.floor_number = None
        self.prop_type = "house" 

        #raise NotImplementedError
    # To be implemented

          

class Apartment(Property):

    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        floor_number: int,
                        floor_area: int,
                        price: int,
                        property_features: List[str],
                        coordinates: Tuple[float, float]):
        super().__init__(prop_id,bedrooms,bathrooms,parking_spaces,full_address,floor_area,price,property_features,coordinates)  
        self.floor_number=floor_number 
        self.land_area = None
        self.prop_type = "apartment"               
 
    

if __name__ == '__main__':
    pass

