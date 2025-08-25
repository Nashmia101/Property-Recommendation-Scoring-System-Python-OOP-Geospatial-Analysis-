from typing import List
from parent_property import Property
from amenity import Amenity

def normalise_scores(list_of_scores: List[float]) -> List[float]:
    s_min = min(list_of_scores)
    s_max = max(list_of_scores)

    normalised_scores = []
    for score in list_of_scores:
        n_score = 1 + (4 * (score - s_min)/(s_max - s_min))
        normalised_scores.append(round(n_score,1))

    return normalised_scores

def score_property(prop: Property, amenities: List[Amenity], amenity_accessibility: dict):
    distances = {}
    weights = {}
    values = {'walk': 3, 'cycle': 2, 'drive': 1, 'optional':0}
    for k, v in amenity_accessibility.items():

        if k == 'medical_centre':
            weights[k] = values[v]
            _,distances[k] = prop.nearest_amenity(amenities, 'medical_centre', None)

        elif k == 'train_station':
            weights[k] = values[v]
            _,distances[k] = prop.nearest_amenity(amenities, 'train_station', None)

        elif k == 'school':
            # If its a school, the value is a dictionary
            if 'school_type' in v.keys():
                school_type = v['school_type']
            else:
                school_type = None
            weights[k] = values[v['accessibility']]
            _, distances[k] = prop.nearest_amenity(amenities, 'school', school_type)

        elif k == 'sport_facility':
            # If its a sport facility, the value is a dictionary
            if 'sport_played' in v.keys():
                sport_played = v['sport_played']
            else:
                sport_played = None
            weights[k] = values[v['accessibility']]
            _, distances[k] = prop.nearest_amenity(amenities, 'sport_facility', sport_played)

    s_i_score = 0
    for key, value in weights.items():
        s_i_score += (distances[key] * value)

    return s_i_score
