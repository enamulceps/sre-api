import requests, subprocess, time

while True:
    try:
        r = requests.get("http://localhost:5000/health")
        if r.status_code != 200:
            subprocess.run(["podman", "restart", "my-api"])
    except Exception:
        subprocess.run(["podman", "restart", "my-api"])
    time.sleep(10)
