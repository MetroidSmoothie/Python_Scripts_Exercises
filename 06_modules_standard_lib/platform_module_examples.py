# Used to access OS & hardware data to obtain info about machine
#       Gets system info so script knows how to behave in running OS

import platform

print("\n Processor name is: {}".format(platform.processor()))
print("\n Python compiler is: {}".format(platform.python_compiler()))
print("\n Operating System is: {}".format(platform.system()))
print("\n OS version is: {}".format(platform.version()))
print("\n OS architecture is: {}".format(platform.architecture()))
