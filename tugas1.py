import tkinter as tk
from tkinter import messagebox

def prediksi_prodi():
    try:
        
        nilai_matematika = float(entry_matematika.get())
        nilai_bahasa_indonesia = float(entry_bahasa_indonesia.get())
        nilai_bahasa_inggris = float(entry_bahasa_inggris.get())
        nilai_fisika = float(entry_fisika.get())
        nilai_kimia = float(entry_kimia.get())
        nilai_biologi = float(entry_biologi.get())
        nilai_geografi = float(entry_geografi.get())
        nilai_sejarah = float(entry_sejarah.get())
        nilai_sosiologi = float(entry_sosiologi.get())
        nilai_ekonomi = float(entry_ekonomi.get())

        
        total_nilai = (nilai_matematika + nilai_bahasa_indonesia + nilai_bahasa_inggris +
                       nilai_fisika + nilai_kimia + nilai_biologi +
                       nilai_geografi + nilai_sejarah + nilai_sosiologi +
                       nilai_ekonomi) / 10

        if total_nilai >= 85:
            hasil = "Rekomendasi: Prodi Teknik"
        elif total_nilai >= 70:
            hasil = "Rekomendasi: Prodi Sains"
        else:
            hasil = "Rekomendasi: Prodi Seni"

        label_hasil.config(text=hasil)
    except ValueError:
        messagebox.showerror("Input Error", "Silakan masukkan nilai yang valid.")


root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")


root.geometry("350x760")


label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
label_judul.pack(pady=10)


mata_pelajaran = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", 
    "Fisika", "Kimia", "Biologi", 
    "Geografi", "Sejarah", "Sosiologi", "Ekonomi"
]


for pelajaran in mata_pelajaran:
    frame = tk.Frame(root)
    frame.pack(pady=5)  

    label = tk.Label(frame, text=f"Nilai {pelajaran}:")
    label.pack()

    entry = tk.Entry(frame, width=20, justify='center')  
    entry.pack(pady=5)  
    if pelajaran == "Matematika":
        entry_matematika = entry
    elif pelajaran == "Bahasa Indonesia":
        entry_bahasa_indonesia = entry
    elif pelajaran == "Bahasa Inggris":
        entry_bahasa_inggris = entry
    elif pelajaran == "Fisika":
        entry_fisika = entry
    elif pelajaran == "Kimia":
        entry_kimia = entry
    elif pelajaran == "Biologi":
        entry_biologi = entry
    elif pelajaran == "Geografi":
        entry_geografi = entry
    elif pelajaran == "Sejarah":
        entry_sejarah = entry
    elif pelajaran == "Sosiologi":
        entry_sosiologi = entry
    elif pelajaran == "Ekonomi":
        entry_ekonomi = entry


button_prediksi = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi)
button_prediksi.pack(pady=10)


label_hasil = tk.Label(root, text="", font=("Arial", 12))
label_hasil.pack(pady=10)


root.mainloop()