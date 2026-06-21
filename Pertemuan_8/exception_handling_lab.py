class ErrorSaldoTidakCukup(Exception):
    pass


class Rekeningbank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo
    
    def tariksaldo(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah Penarikan Harus Lebih Dari 0")

        if jumlah > self.saldo:
            raise ErrorSaldoTidakCukup(
                f"Penarikan Ditolak!, Sisa Saldo anda hanya tersisa Rp.{self.saldo:,}"
            )
        self.saldo -= jumlah
        print(f"\nPenarikan Berhasil, Penarikan dengan nominal Rp{jumlah}")
        print(f"Sisa Saldo anda : Rp{self.saldo}")

print("===== SELAMAT DATANG DI BANK =====")
rekening = Rekeningbank("Ihsan", 1000000)

try:
    print (f"Nama Pemilik :{rekening.nama}")
    print (f"Saldo Anda :{rekening.saldo}")

    jumlah_tarik = int(input("\n Masukkan Nominal yang ingin anda tarik : Rp"))

    rekening.tariksaldo(jumlah_tarik)

except ErrorSaldoTidakCukup as e:
    print("\n[Error Saldo]")
    print(e)

except ValueError as e:
    print ("\n[Error Input]")
    print(e)

finally:
    print ("\n Transaksi anda telah sukses dilakukan")    