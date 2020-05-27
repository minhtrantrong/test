import sys
print("Test sys.argv")
if (len(sys.argv) == 2):
    print("arg 1: ", sys.argv[1])
elif (len(sys.argv) == 3):
    print("arg 2: ", sys.argv[2])
