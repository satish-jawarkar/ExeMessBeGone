import psutil

# Get all running processes
for proc in psutil.process_iter():
    try:
        # Check if the process is a Python script
        if proc.name().lower() == "python":
            proc.terminate()  # Terminate the process
            print(f"Terminated process {proc.pid}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass  # Ignore errors


import subprocess

# Terminate all Python processes
subprocess.run(["taskkill", "/f", "/im", "python.exe"], capture_output=True, text=True)
print("All Python processes terminated.")




import psutil

# List of processes to exclude from termination
excluded_processes = ["system", "idle", "taskmgr", "explorer"]

# Get all running processes
for proc in psutil.process_iter():
    try:
        # Check if the process should be terminated
        if proc.name().lower() not in excluded_processes:
            proc.terminate()  # Terminate the process
            print(f"Terminated process {proc.pid}: {proc.name()}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass  # Ignore errors
