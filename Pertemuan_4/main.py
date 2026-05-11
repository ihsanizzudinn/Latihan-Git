class mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
    def __str__(self):
        return f"Nilai {self.nama} adalah {self.nilai}"

    def __eq__(self, other):
        return self.nilai == other

    def __lt__(self, other):
        return self.nilai < other 
    
    def __gt__(self, other):
        return self.nilai > other
    
mahasiswa1 = mahasiswa ("Ahmad", 100)
mahasiswa2 = mahasiswa ("Ihsan", 80)
mahasiswa3 = mahasiswa ("Udin", 80)

print(mahasiswa1)
print(mahasiswa2)
print(mahasiswa3)

print("=== Perbandingan ===")

print("Ahmad mempunyai nilai yang sama dengan Udin : ", mahasiswa1 == mahasiswa3)
print("Ahmad mempunyai nilai yang lebih besar dari Ihsan : ", mahasiswa1 > mahasiswa2)
print("Ihsan mempunyai nilai yang lebih kecil dari Udin : ", mahasiswa1 == mahasiswa3)

    