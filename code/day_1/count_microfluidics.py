
# Naive example
c = 0
with open('example.txt', encoding="utf8") as o:
    for l in o.readlines():
        if "microfluidics" in l:
            c += l.count("microfluidics")
        elif "Microfluidics" in l:
            c += l.count("Microfluidics")
        elif "MICROFLUIDICS" in l:
            c += l.count("MICROFLUIDICS")


print(f"NAIVE: Found {c} occurences of microfluidics in the text")

# Advanced example
import os
import sys

cc = 0
words = ["microfluidics", "Microfluidics", "MICROFLUIDICS"]
if os.path.exists(sys.argv[1]):
    with open(sys.argv[1], encoding="utf8") as o:
        for l in o.readlines():
            cc += sum([l.count(w) for w in words])

print(f"\nADVANCED: Found {cc} occurences of microfluidics in the text")