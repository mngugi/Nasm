import usb.core

# USB device vendor and product IDs
VENDOR_ID = 0x8087
PRODUCT_ID = 0x8000

dev = usb.core.find(idVendor=0x8087, idProduct=0x8000)

if dev is None:
    raise ValueError('Device not found')

# Perform USB communication here

print(dev)


