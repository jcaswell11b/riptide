import os
import sys, subprocess

try:
  subprocess.call(["ps","aux"])
except:
  print("error")
