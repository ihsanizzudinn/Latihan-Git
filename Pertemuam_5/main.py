class akun_google:
    def __init__ (self, nama, email, password, umur, jenis_kelamin):
        self.nama = nama
        self.email = email
        self.__password = password
        self.__umur = umur
        self.__jenis_kelamin = jenis_kelamin    
    def get_umur(self):
        return self.__umur
    
    def get_jenis_kelamin(self):
        return self.__jenis_kelamin
    
    def login(self, input_pw):
        if input_pw == self.__password:
            print("Login berhasil")
            return True
    
        else:
            print("Password salah")
            return False

    def output_akhir(self, input_pw):
        if self.login(input_pw):
            print (f"Nama : {self.nama}")
            print (f"Email : {self.email}")
            print (f"Umur : {self.__umur}")
            print (f"Jenis Kelamin : {self.__jenis_kelamin}")

        else:
            print("Akses diblokir")

akun1 = akun_google("ihsan", "akungw@gmail.com", "11111", 19, "Laki - Laki")

print("==== LOGIN KE AKUN GOOGLE ANDA ====")
print("MASUKKAN NAMA EMAIL : akungw@gmail.com")
print("PASSWORD : 00000 ")
akun1.output_akhir("00000")

print("==== LOGIN KE AKUN GOOGLE ANDA ====")
print("MASUKKAN NAMA EMAIL : akungw@gmail.com")
print("PASSWORD : 00000 ")
akun1.output_akhir("11111")

print("\n ==== GATTER ====")
print("Umur : ", akun1.get_umur())
print("Jenis kelamin : ", akun1.get_jenis_kelamin())