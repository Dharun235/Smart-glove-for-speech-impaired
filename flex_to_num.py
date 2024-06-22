import joblib

# Load the saved model
model = joblib.load("enter the path") # Extra trees classifier

# Flex sensor values to decimal number convertor
def flex_to_num(data):
    prediction = model.predict(data)        
    return prediction
