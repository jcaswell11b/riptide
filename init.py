import os
import sy

try:
  subprocess.call(["ps","aux"])
  print("")
  os.system("free -m")
except:
  print("error")
