import os
import sys,subprocess

try:
  subprocess.call(["ps","aux"])
  print("")
  os.system("free -m")
except:
  print("error")
