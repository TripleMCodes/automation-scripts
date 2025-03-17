# Pomodoro Timer with Reward System 🎯⏳

## 📌 Overview

This is a **CLI-based Pomodoro Timer** that helps you stay productive while rewarding you with videos, music, or images after each session. It follows the **Pomodoro technique**, alternating between work and break periods.

## 🚀 Features

✅ Customizable work & break durations\
✅ Short & long breaks (long break after every 4 sessions)\
✅ Reward system with **videos, music, or images** 🎥🎵🖼️\
✅ **Automatically closes reward media** after break time\
✅ Saves session history to `sessions.csv`\
✅ Clean **real-time countdown** in the terminal

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TripleMCodes/automation-scripts
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Pomodoro timer**:
   ```bash
   python pomodoro_with_reward_system.py
   ```

## 🎮 How to Use

1. **Set your work and break durations** when prompted.
2. **Choose whether to start a session**.
3. **Focus on work** while the timer counts down.
4. **Take a break** when the timer finishes.
5. **Enjoy a reward** (video, music, or image) if selected.
6. **Session progress is logged**, and you can quit at any time.

## 📂 File Structure

```
📂 pomodoro-project.py
├── pomodoro_with_reward_system.          # Main script
├── sessions.csv       # Logs completed Pomodoro sessions
├── file_types.py      # Defines file categories for rewards
├── rewards/           # Folder containing videos, music, and images
├── README.md          # Documentation
```

## ⚡ Future Improvements

- Add **a GUI version** using Tkinter or PyQt 🎨
- Include **motivational sound alerts** when work time starts 🔊
- Track **weekly & monthly productivity stats** 📊

## 📜 License

This project is **open-source** and free to use. Contributions are welcome!

👨‍💻 Developed by [Connor Connorson]\
🔗 GitHub: [[GitHub - TripleMCodes](https://github.com/TripleMCodes/automation-scripts)]
