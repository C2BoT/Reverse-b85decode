import base64

import marshal

# Create a Python object to be encoded

data = "hello"

# Serialize the Python object into a bytes-like object

serialized_data = marshal.dumps(data)

# Encode the serialized data using Base85

encoded_data = base64.b85encode(serialized_data)

# Write the encoded data to a file

#with open(f'hello.py', 'wb') as f:

#    f.write(encoded_data)

#________

#print

print(encoded_data)

    
