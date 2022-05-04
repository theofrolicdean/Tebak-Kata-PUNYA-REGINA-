from random import choice

KATA = [
    "kasur",
    "bunga",
    "mangkok",
    "piring",
    "bangku",
    "sandal",
    "sepatu",
    "laptop",
    "lemari",
    "boneka",
    "jendela",
    "pintu",
    "garasi",
    "mobil",
    "sepeda",
    "biola",
    "gitar",
    "karet",
    "lebah",
    "beruang"
]
main = True
skor = 0

while main:
    kata_tebakan = choice(KATA)
    tebak = ""
    jumlah_tebakan = 0
    batas_tebakan = 5
    tebakan_habis = False

    print("\nTebak Kata")
    print("10 MIPA 1 - Regina Jayanti Purnama Halim (17)")

    while tebak != kata_tebakan and not tebakan_habis:
        if jumlah_tebakan < batas_tebakan:
            tebak = input("Masukan tebakan: ").lower()
            jumlah_tebakan += 1
        else:
            tebakan_habis = True
    if tebakan_habis:
        print("Kamu gagal tebak.")
        print(f"Katanya adalah {kata_tebakan}")
    else:
        print("Selamat! Kamu berhasil tebak!")
        skor += 1

    mainlagi = input("Main lagi? (ya/tidak): ").lower()

    if mainlagi == "ya":
        continue
    elif mainlagi == "tidak":
        break
    else:
        print("Pilih yang benar sayang... :) lagi aja yuk")

print("Terima kasih sudah bermain... EHEHHE")
print(f"Total skormu: {skor}")
