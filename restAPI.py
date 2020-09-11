import requests # modul untuk mendapatkan hasil dari API web

BANK = input("Mohon masukkan nama bank pilihan Anda (semua dalam huruf kecil): ") # input user untuk nama bank
OPTION = input("Silahkan pilih salah satu opsi (angka) di bawah ini: \n 1. Konversi IDR ke mata uang asing \n 2. Konversi mata uang asing ke IDR \n") # input user untuk opsi konversi

if OPTION == "1": # klausul jika user memilih opsi 1
    CURRENCY = input("Masukkan mata uang asing pilihan Anda (semua dalam huruf kecil) : ")
    AMOUNT = int(input("Masukkan jumlah mata uang IDR Anda (hanya angka) : "))
elif OPTION == "2": # klausul jika user memilih opsi 2
    CURRENCY = input("Masukkan mata uang asing pilihan Anda (semua dalam huruf kecil) : ")
    AMOUNT = int(input("Masukkan jumlah mata uang IDR Anda (hanya angka) : "))
else: # klausul jika user salah input, maka akan memunculkan error dan memaksa user untuk menjalankan program ulang
    raise ValueError("Mohon hanya masukkan angka '1' atau '2'!")

url = requests.get(f"https://api.kurs.web.id/api/v1?token=KlXplCuMvBMxvyTLhsJRJWnQ4PaYap6nXn7WXJ1M&bank={BANK}&matauang={CURRENCY}") # akses api web
sell, buy = url.json()["jual"], url.json()["beli"] # variabel "sell" untuk opsi konversi 1, variabel "buy" untuk opsi konversi 2

# mencetak hasil
print(f"Nilai uang Anda ({(AMOUNT):,} Rupiah) dalam {CURRENCY.upper()} adalah {round((AMOUNT / sell), 2):,}") if OPTION == "1" else print(f"Nilai uang Anda ({(AMOUNT):,} {CURRENCY.upper()}) dalam Rupiah adalah {round((AMOUNT * buy), 2):,}")