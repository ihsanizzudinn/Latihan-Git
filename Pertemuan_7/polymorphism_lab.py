class AlatPembayaran:
    def proses_bayar(self, jumlah):
        print(f"Memproses pembayaran sebesar Rp{jumlah}")


class KartuKredit(AlatPembayaran):
    def proses_bayar(self, jumlah):
        print(f"Pembayaran Rp{jumlah} menggunakan Kartu Kredit berhasil.")


class EWallet(AlatPembayaran):
    def proses_bayar(self, jumlah):
        print(f"Pembayaran Rp{jumlah} menggunakan E-Wallet berhasil.")


class TransferBank(AlatPembayaran):
    def proses_bayar(self, jumlah):
        print(f"Pembayaran Rp{jumlah} menggunakan Transfer Bank berhasil.")


def jalankan_transaksi(objek, jumlah):
    objek.proses_bayar(jumlah)


kartu = KartuKredit()
ewallet = EWallet()
transfer = TransferBank()

jalankan_transaksi(kartu, 50000)
jalankan_transaksi(ewallet, 75000)
jalankan_transaksi(transfer, 100000)