#GUI Calculator Creted By Suvam. Its Help To Calculate ADs team per week top 10 person bonus. 

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

class GRPAdsBonusCalculator:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("GRP ADs Bonus Calculator (Created By Suvam)")
        self.root.geometry("600x400")

        # Set the theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.total_ads_label = ctk.CTkLabel(self.root, text="Enter total ADs:", font=("Arial", 14))
        self.total_ads_label.pack(pady=20)

        # Increase the length of the typing box
        self.total_ads_entry = ctk.CTkEntry(self.root, font=("Arial", 14), width=250)
        self.total_ads_entry.pack(pady=10)

        self.option_var = ctk.IntVar()
        self.option_var.set(0)

        self.option_label = ctk.CTkLabel(self.root, text="Choose an option:", font=("Arial", 14))
        self.option_label.pack(pady=10)

        self.option_frame = ctk.CTkFrame(self.root)
        self.option_radio1 = ctk.CTkRadioButton(self.option_frame, text="$250", variable=self.option_var, value=1, font=("Arial", 12))
        self.option_radio1.pack(side=tk.LEFT, padx=10)
        self.option_radio2 = ctk.CTkRadioButton(self.option_frame, text="$200", variable=self.option_var, value=2, font=("Arial", 12))
        self.option_radio2.pack(side=tk.LEFT, padx=10)
        self.option_frame.pack(pady=10)

        self.button_frame = ctk.CTkFrame(self.root)
        self.button_frame.pack(pady=10, fill="x")

        self.calculate_button = ctk.CTkButton(self.button_frame, text="Calculate", font=("Arial", 14), command=self.calculate_amount)
        self.calculate_button.pack(side=tk.LEFT, fill="x", expand=True, padx=10)

        self.run_again_button = ctk.CTkButton(self.button_frame, text="Run again", font=("Arial", 14), command=self.run_again)
        self.run_again_button.pack(side=tk.LEFT, fill="x", expand=True, padx=10)

        self.goodbye_button = ctk.CTkButton(self.button_frame, text="Goodbye", font=("Arial", 14), command=self.goodbye)
        self.goodbye_button.pack(side=tk.LEFT, fill="x", expand=True, padx=10)

        self.total_amount_label = ctk.CTkLabel(self.root, text="", font=("Arial", 14))
        self.total_amount_label.pack(pady=10)

    def calculate_amount(self):
        try:
            a = int(self.total_ads_entry.get())
            if self.option_var.get() == 1:
                total_amount = a * 250
            elif self.option_var.get() == 2:
                total_amount = a * 200
            else:
                messagebox.showerror("Invalid choice", "Please select an option")
                return
            self.total_amount_label.configure(text=f"Total Amount is: {total_amount}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number of ADs")

    def run_again(self):
        self.total_ads_entry.delete(0, tk.END)
        self.total_amount_label.configure(text="")
        self.option_var.set(0)

    def goodbye(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GRPAdsBonusCalculator()
    app.run()
