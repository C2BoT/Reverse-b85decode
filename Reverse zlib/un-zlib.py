import zlib

# Define the compressed data
compressed_data = b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5OKK)\xcb1442\xd0O,\xd0\xcfM\xcc\xcc\xd3\xcfJ\x03\x001"\x13\xc6'

# Decompress the compressed data
decompressed_data = zlib.decompress(compressed_data)

# Print the decompressed data
print(f"Decompressed data: {decompressed_data}")
