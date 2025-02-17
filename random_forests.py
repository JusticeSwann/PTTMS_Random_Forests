import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import numpy as np
import json
from geopy.distance import geodesic
from sklearn.cluster import DBSCAN
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib