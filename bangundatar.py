import tkinter as tk

root = tk.Tk()
root.title("Kalkulator")
root.resizable(False, False)

layar = tk.Entry(root, font=("Arial", 20), justify="right", width=16)
layar.grid(row=0, column=0, columnspan=4, padx=8, pady=8)


def klik(ch):
    layar.insert("end", ch)


def hapus():
    layar.delete(0, "end")


def hitung():
    try:
        hasil = eval(layar.get())
        layar.delete(0, "end")
        layar.insert(0, str(hasil))
    except Exception:
        layar.delete(0, "end")
        layar.insert(0, "Error")


tombol = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
]

for i, t in enumerate(tombol):
    if t == "=":
        perintah = hitung
    else:
        perintah = lambda x=t: klik(x)
    tk.Button(root, text=t, width=4, height=2, font=("Arial", 14),
              command=perintah).grid(row=1 + i // 4, column=i % 4, padx=2, pady=2)

tk.Button(root, text="C", font=("Arial", 14), command=hapus).grid(
    row=5, column=0, columnspan=4, sticky="we", padx=2, pady=4)

root.mainloop()
