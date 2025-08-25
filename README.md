Property Recommendation & Scoring System
Overview

This project implements a property recommendation engine using Python and Object-Oriented Programming (OOP). Properties (houses, apartments) and amenities (schools, train stations, medical centres, sports facilities) are modelled as classes. The system ingests datasets, processes geospatial data using the Haversine formula, scores properties based on user-defined preferences, and outputs ranked recommendations.

Key Features

Data Ingestion – Load property and amenity datasets from CSV/JSON files (ingestion.py).

Object-Oriented Models – Classes for properties (parent_property.py, child_properties.py) and amenities (amenity.py).

Geospatial Distance Calculation – Nearest amenity lookup using the Haversine formula (haversine.py).

Property Scoring – Compute and normalise scores for amenities accessibility (score.py).

User Request Matching – Parse JSON user requests, filter properties, and produce ranked responses (task6.py).

Feature Engineering – Add/remove property features and extract structured details (task2.py, task3.py).

Exploratory Utilities – Validate data ingestion and amenity distribution (task4.py, task1.py).

Tools & Techniques

Python (OOP, Inheritance, Typing)

CSV & JSON Parsing

Geospatial Analysis (Haversine Distance)

Ranking & Scoring Algorithms

Modular Software Design

Files

amenity.py – Amenity class

child_properties.py – House and Apartment classes

parent_property.py – Abstract Property class and shared methods

ingestion.py – Data ingestion pipeline for properties and amenities

score.py – Property scoring and normalisation

task6.py – Full request–response pipeline with ranked JSON output

task1.py, task2.py, task3.py, task4.py – Data processing, feature engineering, and testing scripts

haversine.py – Distance calculation helper

Author

Nashmia Shakeel

