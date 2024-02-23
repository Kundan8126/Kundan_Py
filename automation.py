# import tkinter as tk

# class HomeAutomationApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Home Automation")
        
#         # Light status
#         self.light_status = False
        
#         # Temperature
#         self.temperature = 20

#         # Light control frame
#         self.light_frame = tk.LabelFrame(master, text="Lights", padx=10, pady=10)
#         self.light_frame.grid(row=0, column=0, padx=10, pady=10)

#         self.light_label = tk.Label(self.light_frame, text="Light is off", fg="red")
#         self.light_label.pack()

#         self.light_button = tk.Button(self.light_frame, text="Turn On", command=self.toggle_light)
#         self.light_button.pack()

#         # Temperature control frame
#         self.temperature_frame = tk.LabelFrame(master, text="Temperature", padx=10, pady=10)
#         self.temperature_frame.grid(row=0, column=1, padx=10, pady=10)

#         self.temperature_label = tk.Label(self.temperature_frame, text=f"Temperature: {self.temperature} °C")
#         self.temperature_label.pack()

#         self.temp_up_button = tk.Button(self.temperature_frame, text="Increase", command=self.increase_temperature)
#         self.temp_up_button.pack()

#         self.temp_down_button = tk.Button(self.temperature_frame, text="Decrease", command=self.decrease_temperature)
#         self.temp_down_button.pack()

#     def toggle_light(self):
#         self.light_status = not self.light_status
#         if self.light_status:
#             self.light_label.config(text="Light is on", fg="green")
#             self.light_button.config(text="Turn Off")
#         else:
#             self.light_label.config(text="Light is off", fg="red")
#             self.light_button.config(text="Turn On")

#     def increase_temperature(self):
#         self.temperature += 1
#         self.temperature_label.config(text=f"Temperature: {self.temperature} °C")

#     def decrease_temperature(self):
#         self.temperature -= 1
#         self.temperature_label.config(text=f"Temperature: {self.temperature} °C")

# def main():
#     root = tk.Tk()
#     app = HomeAutomationApp(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()

import tkinter as tk
from tkinter import ttk

class HomeAutomationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Home Automation")

        # Light status
        self.light_status = False

        # Temperature
        self.temperature = 25

        # Create style
        self.style = ttk.Style()

        # Light control frame
        self.light_frame = ttk.LabelFrame(master, text="Lights", padding=(10, 10))
        self.light_frame.grid(row=0, column=0, padx=10, pady=10)

        self.light_label = ttk.Label(self.light_frame, text="Light is off", foreground="red", font=("Helvetica", 12, "bold"))
        self.light_label.grid(row=0, column=0, padx=5, pady=5)

        self.light_button = ttk.Button(self.light_frame, text="Turn On", command=self.toggle_light, style="LightButton.TButton")
        self.light_button.grid(row=1, column=0, padx=5, pady=5)

        # Temperature control frame
        self.temperature_frame = ttk.LabelFrame(master, text="Temperature", padding=(10, 10))
        self.temperature_frame.grid(row=0, column=1, padx=10, pady=10)

        self.temperature_label = ttk.Label(self.temperature_frame, text=f"Temperature: {self.temperature} °C", font=("Helvetica", 12, "bold"))
        self.temperature_label.grid(row=0, column=0, padx=5, pady=5)

        self.temp_up_button = ttk.Button(self.temperature_frame, text="Increase", command=self.increase_temperature, style="TempButton.TButton")
        self.temp_up_button.grid(row=1, column=0, padx=5, pady=5)

        self.temp_down_button = ttk.Button(self.temperature_frame, text="Decrease", command=self.decrease_temperature, style="TempButton.TButton")
        self.temp_down_button.grid(row=2, column=0, padx=5, pady=5)

        # Configure styles
        self.style.configure("LightButton.TButton", foreground="green", font=("Helvetica", 10, "bold"))
        self.style.configure("TempButton.TButton", font=("Helvetica", 10, "bold"))

    def toggle_light(self):
        self.light_status = not self.light_status
        if self.light_status:
            self.light_label.config(text="Light is on", foreground="green")
            self.light_button.config(text="Turn Off", style="LightButton.TButton")
        else:
            self.light_label.config(text="Light is off", foreground="red")
            self.light_button.config(text="Turn On", style="LightButton.TButton")

    def increase_temperature(self):
        self.temperature += 1
        self.temperature_label.config(text=f"Temperature: {self.temperature} °C")

    def decrease_temperature(self):
        self.temperature -= 1
        self.temperature_label.config(text=f"Temperature: {self.temperature} °C")

def main():
    root = tk.Tk()
    app = HomeAutomationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

