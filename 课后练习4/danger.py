import subprocess

subprocess.Popen("echo hi", shell=True)
subprocess.Popen(["echo", "hi"], shell=False)
