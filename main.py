import tkinter as tk
from tkinter import scrolledtext
import subprocess
import ctypes
import sys
import os
import json
import threading

# --- CONFIG
TASKS = {
    "ipconfig": r'"C:\Windows\System32\ipconfig.exe"',
    "Reload Nginx": r'"C:\nginx\nginx.exe" -s reload',  # Change to your nginx path
    "Stop Windows Update": r'"C:\Windows\System32\net.exe" stop wuauserv',
    "Start Windows Update": r'"C:\Windows\System32\net.exe" start wuauserv',
    "List Directory": r"dir"
}

TASK_PREFIX = "MyAdminTask_"
SCHTASKS_PATH = r"C:\Windows\System32\schtasks.exe"

APPDATA_DIR = os.path.join(os.getenv("APPDATA"), "MyAdminGUI")
os.makedirs(APPDATA_DIR, exist_ok=True)
TASKS_FILE = os.path.join(APPDATA_DIR, "tasks_created.json")


# --- FUNCTIONS 
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_command_inside_gui(command):
    """Run command and stream output inside the log box."""
    def task():
        log_box.insert(tk.END, f"> {command}\n", "command")
        log_box.see(tk.END)

        process = subprocess.Popen(command, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   shell=True, text=True)

        for line in process.stdout:
            log_box.insert(tk.END, line)
            log_box.see(tk.END)

        process.wait()
        log_box.insert(tk.END, f"\nProcess finished with exit code {process.returncode}\n\n")
        log_box.see(tk.END)

    threading.Thread(target=task).start()


def initialize_tasks():
    tasks_created = {}
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            tasks_created = json.load(f)

    for name in TASKS.keys():
        tasks_created[name] = True

    with open(TASKS_FILE, "w") as f:
        json.dump(tasks_created, f)


# --- MAIN 
if __name__ == "__main__":
    if not is_admin():
        params = " ".join([f'"{arg}"' for arg in sys.argv])
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, params, None, 1
        )
        sys.exit()

    root = tk.Tk()
    root.title("Admin Command Terminal Inside GUI")
    root.geometry("800x500")
    root.configure(bg="#2c3e50")

    # Sidebar
    sidebar = tk.Frame(root, width=200, bg="#34495e")
    sidebar.pack(expand=False, fill="y", side="left", anchor="nw")

    tk.Label(sidebar, text="Commands", bg="#34495e", fg="white",
             font=("Arial", 14, "bold")).pack(pady=10)

    for display_name in TASKS.keys():
        btn = tk.Button(sidebar, text=display_name, width=20, height=2,
                        bg="#1abc9c", fg="white", font=("Arial", 10, "bold"),
                        relief="flat",
                        command=lambda n=display_name: run_command_inside_gui(TASKS[n]))
        btn.pack(pady=5, padx=10)

    # Main frame (Log)
    main_frame = tk.Frame(root, bg="#ecf0f1")
    main_frame.pack(expand=True, fill="both", side="right")
 
    tk.Label(main_frame, text="Command Output", bg="#ecf0f1",
             font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)

    log_box = scrolledtext.ScrolledText(main_frame, bg="#1e272e", fg="white",
                                        font=("Consolas", 11), wrap=tk.WORD)
    log_box.pack(fill="both", expand=True, padx=10, pady=5)

    log_box.tag_config("command", foreground="#f39c12", font=("Consolas", 10, "bold"))

    log_box.insert(tk.END, "Initializing terminal...\n")
    root.update()
    initialize_tasks()

    root.mainloop()
