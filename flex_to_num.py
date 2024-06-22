# Flex sensor values to decimal number convertor
def flex_to_num(int_data):

    # Define the ranges and corresponding return values for each item
    ranges = [
        [(260, 271, 0), (276, 290, 1)], # Ranges for item 1
        [(470, 480, 0), (458, 468, 1)], # Ranges for item 2
        [(390, 480, 0), (230, 360, 1)], # Ranges for item 3
        [(432, 450, 0), (410, 428, 1)], # Ranges for item 4
        [(532, 540, 0), (520, 530, 1)], # Ranges for item 5
    ]

    # Initialize a list to store the results of range checks
    results = []
    
    # Iterate over each item in the input list and its corresponding ranges
    for i, item in enumerate(int_data):
        for low, high, val in ranges[i]:
            if low <= item <= high:
                results.append(val)
                break
        else:
            results.append(None) # Append None if no range matches
    
    # Check if all results are valid (i.e., no None values)
    if None in results:
        return "Invalid range for some item(s)"
    
    else:
        # Calculate the final value using the specified formula
        final_value = (2**4 * results[4] + 
                       2**3 * results[3] + 
                       2**2 * results[2] + 
                       2**1 * results[1] + 
                       2**0 * results[0])
    
        return final_value