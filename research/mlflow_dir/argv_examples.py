import sys

alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

args = sys.argv
print(args[0])
print(args[1])
print(args[2])