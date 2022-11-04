import re

with open('output.txt') as f:
    lines = f.readlines()
    p = r': b\'([\d.]+)'
    # floats = [float(i) for i in p.findall(a)]  # Convert strings to float
    # print(floats)
    for line in lines:
        # print(p)
        print((p, line)[1])