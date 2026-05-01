import subprocess

def run(cmd):
    return subprocess.getoutput(cmd)

def check():
    print("📡 IMS DIAGNOSTICS")

    log = run("logcat -d | grep -i ims | tail -50")

    if "REGISTRATION" in log:
        print("✔ IMS registration attempts found")
    else:
        print("❌ No IMS registration detected")

    if "ERROR" in log:
        print("⚠ IMS errors detected:")
        print(log)

    print("\n📶 IWLAN check:")
    print(run("getprop persist.data.iwlan.enable"))

if __name__ == "__main__":
    check()
