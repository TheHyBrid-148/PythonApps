import tkinter as tk
import time


class TimerStopwatchClock:
    def __init__(self, master):
        self.master = master
        master.title("Timer, Stopwatch, Clock")
        master.geometry("400x150")
        master.configure(bg="black")

        self.timer_label = tk.Label(master, text="00:00:00", font=("Arial", 30))
        self.stopwatch_label = tk.Label(master, text="00:00:00", font=("Arial", 30))
        self.clock_label = tk.Label(master, text="", font=("Arial", 30))

        self.start_timer = tk.Button(master, text="Start", command=self.start_timer)
        self.stop_timer = tk.Button(master, text="Stop", command=self.stop_timer)
        self.reset_timer = tk.Button(master, text="Reset", command=self.reset_timer)
        self.start_stopwatch = tk.Button(master, text="Start", command=self.start_stopwatch)
        self.stop_stopwatch = tk.Button(master, text="Stop", command=self.stop_stopwatch)
        self.reset_stopwatch = tk.Button(master, text="Reset", command=self.reset_stopwatch)

        self.timer_label.grid(row=0, column=0, padx=10, pady=10)
        self.stopwatch_label.grid(row=1, column=0, padx=10, pady=10)
        self.clock_label.grid(row=2, column=0, padx=10, pady=10)

        self.start_timer.grid(row=0, column=1, padx=10, pady=10)
        self.stop_timer.grid(row=0, column=2, padx=10, pady=10)
        self.reset_timer.grid(row=0, column=3, padx=10, pady=10)
        self.start_stopwatch.grid(row=1, column=1, padx=10, pady=10)
        self.stop_stopwatch.grid(row=1, column=2, padx=10, pady=10)
        self.reset_stopwatch.grid(row=1, column=3, padx=10, pady=10)

        self.timer_running = False
        self.timer_start_time = None
        self.stopwatch_running = False
        self.stopwatch_start_time = None

    def start_timer(self):
        self.timer_running = True
        self.timer_start_time = time.time()
        self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.timer_start_time = None
        self.timer_label.config(text="00:00:00")

    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.timer_start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            milliseconds = int((elapsed_time - seconds) * 100)
            self.timer_label.config(text="{:02d}:{:02d}:{:02d}".format(minutes, seconds, milliseconds))
            self.master.after(10, self.update_timer)

    def start_stopwatch(self):
        self.stopwatch_running = True
        self.stopwatch_start_time = time.time()
        self.update_stopwatch()

    def stop_stopwatch(self):
        self.stopwatch_running = False

    def reset_stopwatch(self):
        self.stopwatch_running = False
        self.stopwatch_start_time = None
        self.stopwatch_label.config(text="00:00:00")

    def update_stopwatch(self):
        if self.stopwatch_running:
            elapsed_time = time.time() - self.stopwatch_start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            milliseconds = int((elapsed_time - seconds) * 60)
            self.stopwatch_label.config(text="{:02d}:{:02d}:{:02d}".format(minutes, seconds, milliseconds))
            self.master.after(10, self.update_stopwatch)

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.master.after(1000, self.update_clock)


root = tk.Tk()
app = TimerStopwatchClock(root)
root.mainloop()
