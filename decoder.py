import binascii
from urllib.parse import urlparse, parse_qs

# Suspicious link input
url = input("Enter the suspicious URL: ")

# Extract parameter 's'
parsed = urlparse(url)
params = parse_qs(parsed.query)
hex_string = params.get("s", [""])[0]

# Convert hex to text
decoded = binascii.unhexlify(hex_string).decode("utf-8", errors="ignore")

print("Decoded link site:")
print(decoded)
