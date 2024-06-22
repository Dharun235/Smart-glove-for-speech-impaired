import joblib

# Load the saved models
model = joblib.load("enter the path") # Extra trees classifier

# Flex sensor values to decimal number convertor
def flex_to_num(int_data):
    prediction = model.predict(input_data)        
    return prediction
