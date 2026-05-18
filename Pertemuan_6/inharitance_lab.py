class Kendaraan:
    def __init__(self):
        print("Inisialisasi Kendaraan")

    def info(self):
        print("Ini adalah kendaraan umum")

class Mobil(Kendaraan):
    def __init__(self):
        super().__init__()
        print("Inisialisasi Mobil")

    def info(self):
        super().info()
        print("Mobil memiliki 4 roda")

class Listrik(Kendaraan):
    def __init__(self):
        super().__init__()
        print("Inisialisasi Kendaraan Listrik")

    def info(self):
        super().info()
        print("Menggunakan tenaga listrik")

class Tesla(Mobil, Listrik):
    def __init__(self):
        super().__init__()
        print("Inisialisasi Tesla")

    def info(self):
        super().info()
        print("Tesla adalah mobil listrik modern")

print("=== Membuat Objek Tesla ===")
mobil_tesla = Tesla()

print("\n=== Menampilkan Informasi ===")
mobil_tesla.info()

print("\n=== Method Resolution Order (MRO) ===")
print(Tesla.__mro__)