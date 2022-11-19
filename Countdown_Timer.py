import threading
import time
import tkinter as tk


class Countdowntimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("650x250")
        self.root.title("Countdown Timer")
        
        self.time_entry = tk.Entry(self.root, font=("Times", 30))
        self.time_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        #Setting the Start button
        self.start_button = tk.Button(self.root, font=("Times", 30), text="Start",command=self.start_thread)
        self.start_button.grid(row=1, column=0, padx=5, pady=5)
        
        #Setting the Pause button
        self.pause_button = tk.Button(self.root, font=("Times", 30), text="Pause",command=self.pause_thread)
        self.pause_button.grid(row=1, column=1, padx=5, pady=5)
        
        #Setting the Resume button
        self.resume_button = tk.Button(self.root, font=("Times", 30), text="Resume",command=self.resume_thread)
        self.resume_button.grid(row=1, column=2, padx=5, pady=5)
        
        #Setting the Reset button
        self.reset_button = tk.Button(self.root, font=("Times", 30), text="Reset",command=self.stop)
        self.reset_button.grid(row=1, column=3, padx=5, pady=5)
        
        #Displaying the remaining time
        self.time_label = tk.Label(self.root, font=("Times", 30), text="00:00:00")
        self.time_label.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        self.stop_loop = True
        self.resume_loop= False
        self.pause_loop = False
        self.hours,self.minutes,self.seconds,self.full_seconds=0,0,0,0
        self.temp = 0

        self.root.mainloop()

    def start_thread(self):
        t = threading.Thread(target=self.start)
        t.start()
        
        
    def pause_thread(self):
        self.pause_loop = True
        self.time_label.config(text=f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
    
    def resume_thread(self):
        self.stop_loop = True
        self.resume_loop = True
        self.pause_loop = False
        self.start()
    
    def stop(self):
        self.stop_loop = True
        self.resume_loop= False
        self.pause_loop = False
        self.time_label.config(text="00:00:00")
    
    def start(self):
        if self.stop_loop:
            if not self.pause_loop and not self.resume_loop:
                self.stop_loop = False
                self.hours,self.minutes,self.seconds=0,0,0
                string_split = self.time_entry.get().split(":")
                if len(string_split) == 3:
                    self.hours = int(string_split[0])
                    self.minutes = int(string_split[1])
                    self.seconds = int(string_split[2])

                elif len(string_split) == 2:
                    self.minutes = int(string_split[0])
                    self.seconds = int(string_split[1])

                elif len(string_split) == 1:
                    self.seconds = int(string_split[0])

                else:
                    print("Invalid time format")
                    return
            
                self.full_seconds = (self.hours*3600) + (self.minutes * 60) + self.seconds

                while self.full_seconds > 0 and not self.stop_loop and not self.resume_loop and not self.pause_loop:
                    self.full_seconds -= 1
                    self.temp = self.full_seconds

                    self.minutes, self.seconds = divmod(self.full_seconds, 60)
                    self.hours, self.minutes = divmod(self.minutes, 60)

                    self.time_label.config(text=f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
                    self.root.update()
                    time.sleep(1)
                    
            if self.resume_loop:
                while self.temp > 0 and not self.pause_loop:
                    self.temp -= 1
                    
                    self.minutes, self.seconds = divmod(self.temp, 60)
                    self.hours, self.minutes = divmod(self.minutes, 60)

                    self.time_label.config(text=f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
                    self.root.update()
                    time.sleep(1)

Countdowntimer()