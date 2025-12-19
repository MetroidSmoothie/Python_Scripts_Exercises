import platform
import os

print("\nThis script will run the proper network config command based on the OS")
systemType = platform.system()
if systemType[0] == "w" or systemType[0] == "W":
    print(f"OS is: {platform.system()}")
    print("Using ipconfig...")
    os.system("ipconfig")
else:
    print(f"OS is: {platform.system()}")
    print("Using ifconfig...")
    os.system("ifconfig")
