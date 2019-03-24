import os
import sys, subprocess

try:
  subprocess.call(["ps","aux"])
  os.system("uname -a")
except:
  print("error")
