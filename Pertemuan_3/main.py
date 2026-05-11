class Karakter:
    def __init__(self, nama, hp):
        self.nama = nama
        self.hp = hp

    def tampilkan_status(self):
        print (f"Nama : {self.nama}")
        print (f"Hp : {self.hp}")

    def kena_damage(self, damage):
        self.hp -= damage
        print (f"{self.nama} terkena damage {damage} sisa HP: {self.hp}" )

    @staticmethod
    def critical_damage(damage):
        return damage * 2
    
karakter1 = Karakter("Hero A", 200)
karakter2 = Karakter("Hero B", 250)

print ("==== MAIN CHARACTER =====")
karakter1.tampilkan_status()
karakter1.kena_damage(20)

print ("\n==== SIDE CHARACTER ====")
karakter2.tampilkan_status()
karakter2.kena_damage(40)

print ("\n ==== CRITICAL DAMAGE RULES ====")
print ("CRITICAL = DAMAGE NORMAL X2")
print ("ex : Normal Damage = 50")
print ("     Damage Critical = ", Karakter.critical_damage(50))

