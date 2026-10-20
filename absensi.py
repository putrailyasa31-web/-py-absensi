
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import date

FILE = "data_absensi.csv"

def simpan_data():
    nama = entry_nama.get().strip()
    status = combo_status.get()
    tanggal = date.today().strftime("%d-%m-%Y")

    if nama == "":
        messagebox.showwarning("Peringatan", "Nama harus diisi!")
        return

    file_baru = not os.path.exists(FILE)

    with open(FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if file_baru:
            writer.writerow(["Nama", "Tanggal", "Status"])

        writer.writerow([nama, tanggal, status])

    tabel.insert("", "end", values=(nama, tanggal, status))
    messagebox.showinfo("Berhasil", "Data berhasil disimpan!")

    entry_nama.delete(0, tk.END)
    combo_status.set("Hadir")


def bersihkan():
    entry_nama.delete(0, tk.END)
    combo_status.set("Hadir")


def muat_data():
    if os.path.exists(FILE):
        with open(FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)

            for baris in reader:
                if len(baris) == 3:
                    tabel.insert("", "end", values=baris)


# Membuat jendela aplikasi
root = tk.Tk()
root.title("Aplikasi Absensi Karyawan")
root.geometry("600x450")
root.configure(bg="#f0f4f8")

judul = tk.Label(
    root,
    text="ABSENSI KARYAWAN",
    font=("Arial", 18, "bold"),
    bg="#f0f4f8"
)
judul.pack(pady=15)

# Form input
frame = tk.Frame(root, bg="#f0f4f8")
frame.pack(pady=5)

tk.Label(frame, text="Nama Karyawan:", bg="#f0f4f8").grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
)

entry_nama = tk.Entry(frame, width=30)
entry_nama.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame, text="Status:", bg="#f0f4f8").grid(
    row=1, column=0, padx=10, pady=10, sticky="w"
)

combo_status = ttk.Combobox(
    frame,
    values=["Hadir", "Izin", "Sakit"],
    state="readonly",
    width=27
)
combo_status.grid(row=1, column=1, padx=10, pady=10)
combo_status.set("Hadir")

# Tombol
frame_tombol = tk.Frame(root, bg="#f0f4f8")
frame_tombol.pack(pady=10)

tk.Button(
    frame_tombol,
    text="Simpan Absensi",
    command=simpan_data,
    bg="#198754",
    fg="white",
    width=15
).grid(row=0, column=0, padx=5)

tk.Button(
    frame_tombol,
    text="Bersihkan",
    command=bersihkan,
    width=12
).grid(row=0, column=1, padx=5)

# Tabel data
kolom = ("Nama", "Tanggal", "Status")

tabel = ttk.Treeview(
    root,
    columns=kolom,
    show="headings",
    height=8
)

for nama_kolom in kolom:
    tabel.heading(nama_kolom, text=nama_kolom)
    tabel.column(nama_kolom, width=170, anchor="center")

tabel.pack(padx=15, pady=10, fill="both", expand=True)

# Menampilkan data yang sudah tersimpan
muat_data()

root.mainloop()
