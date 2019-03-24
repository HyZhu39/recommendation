import sys
import os

os.system("python db.py")
arg = sys.argv[1]
os.system("python excute.py preprocess")
os.system("python excute.py excute "+arg)

