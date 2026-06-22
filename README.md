# OBSERVER 👁️

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Security Focus](https://img.shields.io/badge/focus-Cybersecurity%20Research-red.svg)](###)

**OBSERVER** is a dual-purpose behavioral engineering framework designed to analyze the mechanics of background input monitoring and implement host-based detection mechanisms. Built entirely in Python, it serves as an educational and analytical laboratory framework to demonstrate how low-level OS hooks interact with file systems, while simultaneously simulating Endpoint Detection and Response (EDR) telemetry to catch unauthorized tracking behaviors.

---

## 🛠️ Key Features

* **Asynchronous Input Analysis:** Leverages multi-threaded event-driven listener loops to capture and parse hardware input without blocking the OS interface thread.
* **Heuristic Process Auditing:** Actively scans the host environment to enumerate unprivileged background scripting engines running without a visible GUI context.
* **Behavioral File Guard:** Monitors real-time file system I/O footprints to flag frequent or automated text log modifications typical of data staging tactics.
* **Buffered Memory Architecture:** Stores raw metrics in RAM and dumps them in periodic batches to evade trivial continuous I/O detection routines.

---

## 📋 Installation & Prerequisites

Follow these exact steps to initialize your workspace and install the required dependencies inside Visual Studio Code.

### Step 1: Open the Project Workspace
1. Create a folder named `Observer` on your system.
2. Open VS Code, go to **File > Open Folder...**, and select the `Observer` folder.
3. Open the integrated terminal inside VS Code by pressing `Ctrl + \`` (or `Cmd + \`` on macOS).

### Step 2: Set Up an Isolated Environment
Generate and activate a Python virtual environment to manage dependencies locally without impacting your global system environment:
* **Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1

```

* **Linux / macOS:**
```bash
python -m venv venv
source venv/bin/activate

```



*(Once activated, you will see a `(venv)` prefix appear at the front of your terminal command line prompt).*

### Step 3: Install Required Analysis Modules

Execute the following python wrapper command in your terminal to install the mandatory platform-independent security dependencies:

```bash
python -m pip install pynput psutil watchdog

```

| Dependency | Purpose |
| --- | --- |
| `pynput` | Manages asynchronous system-level event hooks for input parsing. |
| `psutil` | Provides low-level process querying, PID enumeration, and system performance telemetry. |
| `watchdog` | Tracks real-time file-system events to capture live log modifications. |

---

## 🚀 Step-by-Step Execution Guide

### Step 1: Create the Source File

In the VS Code Explorer pane on the left, create a new file named `main.py` and ensure your complete framework script code is saved inside it.

### Step 2: Run the Framework

From your active virtual environment terminal in VS Code, execute the tool:

```bash
python main.py

```

Upon execution, the terminal will print initialization status logs confirming that the concurrent background worker threads are running.

### Step 3: How to Check the Output

The framework delivers output through two channels simultaneously:

1. **Live Console Telemetry:** Keep your eyes on the VS Code terminal. If a background shell interpreter initializes or a script modifies files within your workspace directory, the heuristic rule-set will immediately print a `[SYSTEM NOTICE]` or a `[ALERT]` line directly to your console pane.
2. **Forensic Session Logs:** Look at your project directory on the left. A new text file named `security_capture.txt` will generate automatically. Inside, you will find chronological entry headers containing precise timestamp blocks documenting structural system status.

### Step 4: Graceful Shutdown

To terminate the application safely without risking data loss, press the **`ESC`** key in your terminal workspace context. This triggers a clean break of the OS hook loops and forces an immediate dump of remaining operational memory metrics directly onto the file system before exiting.

---

## ⚖️ Ethical Use Disclaimer

> **IMPORTANT:** This framework is designed and provided strictly as an educational tool for cybersecurity students, researchers, and defense practitioners to study input mechanics and develop heuristic detection rule-sets. It must only be executed in controlled lab settings or on systems where the operator possesses explicit administrative authorization.

```
