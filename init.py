import os
import sys

try:
  subprocess.call(["ps","aux"])
  print("")
  os.system("free -m")
except:
  print("error")
