🖥️ AdminCommandGUI – Windows Admin Command Panel

    AdminCommandGUI is a lightweight Windows application built with Python and Tkinter that lets you execute common administrator-level commands (like restarting services or checking IPs) through a clean and user-friendly      graphical interface.
    
    It runs system commands directly inside a scrollable terminal window — no need to open Command Prompt manually or type repetitive commands again.

✨ Features

    ✅ One-click admin commands – Quickly run predefined Windows system commands like ipconfig, net start, or net stop.  
    ✅ Real-time terminal output – View command execution results directly inside the GUI.  
    ✅ Auto-elevated privileges – Automatically requests Administrator rights when needed.  
    ✅ Threaded execution – Prevents the GUI from freezing during long-running commands.  
    ✅ Customizable task list – Easily modify or add your own commands in the code.  
    ✅ Persistent configuration – Saves data to a JSON file inside %APPDATA%.  



⚙️ How It Works

    1. Select any command from the left sidebar (e.g., “Reload Nginx” or “Stop Windows Update”).
    2. The command runs in the background while output appears in the right-hand terminal.
    3. You can add or edit commands inside the script — no extra setup required.

📦 Tech Stack

    🐍 Python 3.8+
  
    🪟 Tkinter (GUI framework)
  
    ⚙️ ctypes (for admin privileges)
  
    🧵 threading (to keep GUI responsive)
  
    📜 subprocess (for command execution)
  
    💾 JSON (to store task state in %APPDATA%)

🚀 Usage

    1. Run python main.py
    
    2. If prompted, grant Administrator access.
    
    3. Click a command button from the left panel to execute it.
    
    4. View command output in the built-in terminal area.
