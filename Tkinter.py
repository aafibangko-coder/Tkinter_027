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

for i, mapel in enumerate(mata_pelajaran):
    label = tk.Label(
        frame_input,
        text=mapel,
        font=("Arial", 11),
        bg="#F0F4F8",
        width=22,
        anchor="w"
    )
    label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

    entry = ttk.Entry(frame_input, width=25, justify="center")
    entry.grid(row=i, column=1, padx=5, pady=5)

    input_nilai.append(entry)

def hasil_prediksi():
    hasil.config(
        text="Hasil Prediksi: Teknologi Informasi",
        fg="#16803C"
    )

tombol = tk.Button(
    root,
    text="Hasil Prediksi",
    command=hasil_prediksi,
    font=("Arial", 12, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    width=20,
    cursor="hand2",
    relief="flat"
)
tombol.pack(pady=20)

hasil = tk.Label(
    root,
    text="Hasil Prediksi: Belum ada",
    font=("Arial", 13, "bold"),
    bg="#F0F4F8",
    fg="#555555"
)
hasil.pack(pady=10)

root.mainloop()