# ⏳ Study Timer  

## Overview  
This is a simple **Python-based study timer** that allows users to set a study duration in minutes. The timer **counts down** and plays a **beep sound** when the session ends.  

## Features  
- ✅ Accepts **study duration** in minutes.  
- ✅ Displays a **live countdown** in `MM:SS` format.  
- ✅ **Beep alert** when time is up (Windows only).  
- ✅ Handles **manual interruption (Ctrl + C)** gracefully.  

## Prerequisites  
- Python 3.x  
- Works on **Windows** (due to `winsound` module).  
- If using **Linux/macOS**, replace `winsound.Beep` with an alternative (e.g., `os.system("play -nq -t alsa synth 1 sine 1000")`).  

## Installation  
1. Clone the repository:  
   ```sh
   git clone https://github.com/your-username/study-timer.git
   cd study-timer
