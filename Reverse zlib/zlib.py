import zlib

message = b"hello"
compressed_data = zlib.compress(message)

print(compressed_data)
