import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("600x650")
root.resizable(False, False)
root.configure(bg="#F0F4F8")

judul = tk.Label(
    root,
    text="APLIKASI PREDIKSI PRODI PILIHAN",
    font=("Arial", 18, "bold"),
    bg="#F0F4F8",
    fg="#1E3A5F"
)
