class Buku:
    def __init__(self, judul, penulis, penerbit, jumlah_halaman):
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.jumlah_halaman = jumlah_halaman
    
    def info(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis}, Penerbit: {self.penerbit}, Jumlah Halaman: {self.jumlah_halaman}"
    
buku1 = Buku("Bumi", "Tereliye", "Gramedia", 125)
buku2 = Buku("Matahari Minor", "Tereliye", "Gramedia", 150)

print(buku1.info())
print(buku2.info())
