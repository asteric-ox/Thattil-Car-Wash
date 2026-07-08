import os
import sys
import subprocess

if __name__ == "__main__":
    # Change directory to backend to ensure .env and other files are found correctly
    # or just run it with the full path. 
    # Root paths in app.py are now absolute, so we can run it from here.
    
    print("Starting D2 Car Wash Server...")
    print("Frontend: ./frontend")
    print("Backend: ./backend")
    
    try:
        # Run app.py from the backend directory so it has the correct working directory for seeds/data files
        os.chdir('backend')
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\nStopping server...")
    except Exception as e:
        print(f"Error starting server: {e}")
