#%%
# dataset taken is carprice data
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#%% Analysing data
data = pd.read_csv("CarPrice.csv", index_col="car_ID")
print("\ndata set:", data.head())
print("\nColumns name:", data.columns)
print("\nData Types of columns: ", data.dtypes)

# convert compression rato into int
data["compressionratio"] = data["compressionratio"].astype(int) 
convert_dict_door = {"two" : 2, "four" : 4}
data["doornumber"] = data["doornumber"].replace(convert_dict_door)

# binning of "boreratio" and "stroke"

# More consideration on selection of nominal features
# Nominal Catagories includes "fueltype", "carbody", "aspiration"
# "enginelocation", "drivewheel", "fuelsystem"
 
feature_list_transform = ["fueltype", "aspiration", "drivewheel",  "enginetype", "carbody", "enginelocation", "fuelsystem"]
LE = LabelEncoder()
main_dict = dict()

for i in range(len(feature_list_transform)):
    labels = LE.fit(data[ feature_list_transform[i] ])
    data[ feature_list_transform[i] ] = LE.transform(data[ feature_list_transform[i] ])
    temp_dict = dict()
    for index, label in enumerate(LE.classes_):
        temp_dict.update({index : label})

    main_dict.update( {feature_list_transform[i] : temp_dict} )

# Ordinal Features includes cylindernumber
cylindernumber_dict = {"four" : 4, "six" : 6, "five" : 5, "three" : 3, "twelve" : 12, "two" : 2, "eight" : 8 }
data["cylindernumber"].replace(cylindernumber_dict, inplace=True)
main_dict.update({"cylindernumber" : cylindernumber_dict})


