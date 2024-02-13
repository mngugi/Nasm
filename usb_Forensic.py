import usb.core
import hashlib
import time

# USB device vendor and product IDs
VENDOR_ID = 0x8087
PRODUCT_ID = 0x8000

# Find the USB device
dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

if dev is None:
    raise ValueError('Device not found')

# Perform USB communication here

# Generate timestamps
timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# Hashing data from USB device
data = b''  # Sample data received from USB device, replace with actual data
hash_md5 = hashlib.md5(data).hexdigest()
hash_sha2 = hashlib.sha256(data).hexdigest()
hash_sha3 = hashlib.sha3_256(data).hexdigest()

# Printing results
print("Timestamp:", timestamp)
print("MD5 Hash:", hash_md5)
print("SHA-2 Hash:", hash_sha2)
print("SHA-3 Hash:", hash_sha3)
print("USB Device Information:", dev)
