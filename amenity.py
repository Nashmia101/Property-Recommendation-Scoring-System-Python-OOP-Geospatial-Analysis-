# Copy and paste your Amenity class here from the previous task
from typing import Tuple, List, Union

class Amenity():
    def __init__(self, amenity_code: str, 
                        amenity_name: str,
                        amenity_type: str, 
                        amenity_subtype: str,
                        coordinates: Tuple[float, float]):
        #raise NotImplementedError
        self.amenity_code = amenity_code
        self.amenity_name = amenity_name
        self.amenity_type = amenity_type
        self.amenity_subtype = amenity_subtype
        self.amenity_coords = coordinates


    def get_amenity_code(self) -> str:
        return self.amenity_code
        #raise NotImplementedError
    
    def set_amenity_name(self, amenity_name: str) -> None:
        self.amenity_name = amenity_name
        #raise NotImplementedError
    
    def get_amenity_name(self) -> str:
        return self.amenity_name
        #raise NotImplementedError
    
    def get_amenity_coords(self) -> Tuple[float, float]:
        return self.amenity_coords
        #raise NotImplementedError
    
    def get_amenity_type(self) -> str:
        return self.amenity_type
        #raise NotImplementedError
    
    def set_amenity_subtype(self, amenity_subtype: Union[str,None]) -> None:
        self.amenity_subtype = amenity_subtype
        #raise NotImplementedError
    
    def get_amenity_subtype(self) -> Union[str,None]:
        return self.amenity_subtype
        #raise NotImplementedError

if __name__ == '__main__':
    a = Amenity('1001')
    

