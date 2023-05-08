import zlib

# Define the compressed data
compressed_data = b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15'


# Decompress the compressed data
decompressed_data = zlib.decompress(compressed_data)

# Print the decompressed data
print(f"Decompressed data: {decompressed_data}")
