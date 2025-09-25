import subprocess

def check_and_push():
    try:
        # Get latest local commit
        local_commit = subprocess.getoutput("git rev-parse HEAD").strip()

        # Get latest remote commit
        remote_commit = subprocess.getoutput("git rev-parse origin/main").strip()

        print(f"Local Commit : {local_commit}")
        print(f"Remote Commit: {remote_commit}")

        if local_commit == remote_commit:
            print("✅ Project is already pushed to GitHub (local and remote are same).")
        else:
            print("❌ Project is NOT fully pushed.")
            print("📤 Pushing changes to GitHub...")
            
            # Run git push
            push_result = subprocess.getoutput("git push origin main")
            print(push_result)
            
            # Verify again
            remote_commit_after = subprocess.getoutput("git rev-parse origin/main").strip()
            if local_commit == remote_commit_after:
                print("✅ Push successful! Project is now on GitHub.")
            else:
                print("⚠️ Push attempted but commits still differ. Check manually.")
    except Exception as e:
        print("⚠️ Error: Make sure you're inside a Git project folder and 'origin' exists.")
        print(e)

if __name__ == "__main__":
    check_and_push()
