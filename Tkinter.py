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
judul.pack(pady=20)

frame_input = tk.Frame(root, bg="#F0F4F8")
frame_input.pack(padx=40, pady=5)

mata_pelajaran = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Informatika",
    "Fisika",
    "Kimia",
    "Biologi",
    "Ekonomi",
    "Sejarah",
    "Pendidikan Pancasila"
]

input_nilai = []
