# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

#loading the saved model
loaded_model = pickle.load(open('D:/ML Projects/Deploying a ML Model/trained_model.sav', 'rb')) #rb - reading the binary file


input_data = (5,166,72,19,175,25.8,0.587,51) #any input to predict, this is taken from the dataset itself

#changing the input data into numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the array as we are predicting for one instance - #IF WE DONT RESHAPE IT EXPECTS 768 array(total)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1) #reshaping - telling that we are giving 1 array


prediction = loaded_model.predict(input_data_reshaped)
print(prediction) #output should be 0 - non diabetic, ie: predict the outcome as 0

if (prediction[0]==0): #prediction is a list so index is required (has only 1 value in the list anyways)
  print("The person is non-diabetic")
else:
  print("The person is diabetic")