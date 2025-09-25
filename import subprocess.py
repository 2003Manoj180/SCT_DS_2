import subprocess

def is_project_pushed():
    try:
        # Get latest local commit hash
        local_commit = subprocess.getoutput("git rev-parse HEAD").strip()

        # Get latest remote commit hash (from origin/main)
        remote_commit = subprocess.getoutput("git rev-parse origin/main").strip()

        print(f"Local Commit : {local_commit}")
        print(f"Remote Commit: {remote_commit}")

        if local_commit == remote_commit:
            print("✅ Project is pushed to GitHub (local and remote are same).")
        else:
            print("❌ Project is NOT fully pushed. Run: git push")
    except Exception as e:
        print("⚠️ Error: Make sure you're inside a Git project folder and 'origin' exists.")
        print(e)

if __name__ == "__main__":
    is_project_pushed()
