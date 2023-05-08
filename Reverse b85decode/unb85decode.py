import base64
import marshal

encoded_data = "+68E3Y;11"
    
# Decode the Base85-encoded data
decoded_data = base64.b85decode(encoded_data)

# Deserialize the decoded data into a Python object
loaded_object = marshal.loads(decoded_data)

# Print the loaded object to verify its contents
    
print(loaded_object)