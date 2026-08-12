from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import os


dataPendaftar = []


class Pengguna:

    def __init__(self, nama, alamat, nomorTelepon):
        self.nama = nama
        self.alamat = alamat
        self.nomorTelepon = nomorTelepon

    def tampilInfo(self):
        return self.nama


class CalonPelajar(Pengguna):

    def __init__(
        self,
        nama,
        alamat,
        nomorTelepon,
        asalSekolah,
        namaWali
    ):
        super().__init__(nama, alamat, nomorTelepon)

        self.nomorPendaftaran = ""
        self.asalSekolah = asalSekolah
        self.namaWali = namaWali
        self.statusPendaftaran = "Menunggu Verifikasi"

    def daftar(self):
        self.nomorPendaftaran = "GTR-0001"

    def lihatStatus(self):
        return self.statusPendaftaran

    def tampilInfo(self):
        return self.nama + " - Calon Pelajar"


class Admin(Pengguna):

    def __init__(self, username, password):
        super().__init__("", "", "")

        self.username = username
        self.password = password

    def login(self, username, password):
        return username == self.username and password == self.password

    def verifikasiData(self):
        return "Data berhasil diverifikasi"

    def hapusData(self):
        return "Data berhasil dihapus"

    def tampilInfo(self):
        return "Admin - " + self.username


class Pendaftaran:

    def __init__(self):
        self.statusVerifikasi = "Menunggu Verifikasi"

    def simpanData(self):
        print("Data pendaftaran disimpan")

    def verifikasiBerkas(self):
        self.statusVerifikasi = "Terverifikasi"

    def tampilData(self):
        return self.statusVerifikasi


class ServerWeb(BaseHTTPRequestHandler):

    def do_GET(self):

        url = urlparse(self.path)
        path = url.path
        query = parse_qs(url.query)

        if path == "/" or path == "/index.html":
            self.bukaHTML("index.html")

        elif path == "/daftar" or path == "/daftar.html":
            self.bukaHTML("daftar.html")

        elif path == "/berhasil" or path == "/berhasil.html":
            self.bukaBerhasil()

        elif path == "/status":
            nomor = query.get("nomor", [""])[0]
            self.bukaStatus(nomor)

        elif path == "/status.html":
            self.bukaHTML("status.html")

        elif path == "/login" or path == "/login.html":
            self.bukaHTML("login.html")

        elif path == "/admin" or path == "/admin.html":
            self.bukaAdmin()

        elif path == "/terima":
            nomor = query.get("nomor", [""])[0]

            for data in dataPendaftar:
                if data["nomorPendaftaran"] == nomor:
                    data["status"] = "Diterima"
                    break

            self.send_response(303)
            self.send_header("Location", "/admin")
            self.end_headers()

        elif path == "/tolak":
            nomor = query.get("nomor", [""])[0]

            for data in dataPendaftar:
                if data["nomorPendaftaran"] == nomor:
                    data["status"] = "Ditolak"
                    break

            self.send_response(303)
            self.send_header("Location", "/admin")
            self.end_headers()

        else:
            self.send_error(404, "Halaman tidak ditemukan")


    def do_POST(self):

        print("POST MASUK:", self.path)

        panjang = int(self.headers["Content-Length"])
        data = self.rfile.read(panjang).decode("utf-8")
        form = parse_qs(data)

        if self.path == "/login":

            username = form.get("username", [""])[0]
            password = form.get("password", [""])[0]

            admin = Admin("Admin", "loginadmin")

            if admin.login(username, password):
                self.send_response(303)
                self.send_header("Location", "/admin")
                self.end_headers()
            else:
                self.send_response(303)
                self.send_header("Location", "/login")
                self.end_headers()

            return

        elif self.path == "/daftar":

            nama = form.get("nama", [""])[0]
            alamat = form.get("alamat", [""])[0]
            nomorTelepon = form.get("nomorTelepon", [""])[0]
            asalSekolah = form.get("asalSekolah", [""])[0]
            namaWali = form.get("namaWali", [""])[0]
            tanggal = form.get("tanggal", [""])[0]

            calon = CalonPelajar(
                nama,
                alamat,
                nomorTelepon,
                asalSekolah,
                namaWali
            )

            calon.daftar()

            nomor = "GTR-" + str(
                len(dataPendaftar) + 1
            ).zfill(4)

            calon.nomorPendaftaran = nomor

            dataPendaftar.append({
                "nama": nama,
                "alamat": alamat,
                "nomorTelepon": nomorTelepon,
                "asalSekolah": asalSekolah,
                "namaWali": namaWali,
                "tanggal": tanggal,
                "nomorPendaftaran": nomor,
                "status": calon.statusPendaftaran
            })

            print("Pendaftaran berhasil")
            print("Nomor:", nomor)

            self.send_response(303)
            self.send_header("Location", "/berhasil.html")
            self.end_headers()

            return

        else:
            self.send_error(404, "Halaman tidak ditemukan")


    def bukaHTML(self, namaFile):

        lokasi = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "template",
            namaFile
        )

        try:
            with open(lokasi, "r", encoding="utf-8") as file:
                isi = file.read()

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "text/html; charset=utf-8"
            )
            self.end_headers()

            self.wfile.write(isi.encode("utf-8"))

        except Exception as error:
            print("ERROR:", error)
            self.send_error(404, "File HTML tidak ditemukan")


    def bukaBerhasil(self):

        lokasi = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "template",
            "berhasil.html"
        )

        try:
            with open(lokasi, "r", encoding="utf-8") as file:
                isi = file.read()

            if len(dataPendaftar) == 0:
                self.send_error(404, "Belum ada data pendaftaran")
                return

            data = dataPendaftar[-1]

            isi = isi.replace("{{nama}}", data.get("nama", "-"))
            isi = isi.replace("{{alamat}}", data.get("alamat", "-"))
            isi = isi.replace(
                "{{nomorTelepon}}",
                data.get("nomorTelepon", "-")
            )
            isi = isi.replace(
                "{{asalSekolah}}",
                data.get("asalSekolah", "-")
            )
            isi = isi.replace("{{namaWali}}", data.get("namaWali", "-"))
            isi = isi.replace("{{tanggal}}", data.get("tanggal", "-"))
            isi = isi.replace(
                "{{nomorPendaftaran}}",
                data.get("nomorPendaftaran", "-")
            )
            isi = isi.replace("{{status}}", data.get("status", "-"))

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "text/html; charset=utf-8"
            )
            self.end_headers()

            self.wfile.write(isi.encode("utf-8"))

        except Exception as error:
            print("ERROR:", error)
            self.send_error(
                404,
                "File berhasil.html tidak ditemukan"
            )


    def bukaStatus(self, nomor):

        lokasi = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "template",
            "status.html"
        )

        try:
            with open(lokasi, "r", encoding="utf-8") as file:
                isi = file.read()

            data = None

            for pendaftar in dataPendaftar:
                if pendaftar["nomorPendaftaran"] == nomor:
                    data = pendaftar
                    break

            if data:
                isi = isi.replace(
                    "{{nomor}}",
                    data["nomorPendaftaran"]
                )
                isi = isi.replace(
                    "{{nama}}",
                    data["nama"]
                )
                isi = isi.replace(
                    "{{asalSekolah}}",
                    data["asalSekolah"]
                )
                isi = isi.replace(
                    "{{status}}",
                    data["status"]
                )

            else:
                isi = isi.replace("{{nomor}}", nomor)
                isi = isi.replace(
                    "{{nama}}",
                    "Data tidak ditemukan"
                )
                isi = isi.replace("{{asalSekolah}}", "-")
                isi = isi.replace(
                    "{{status}}",
                    "Nomor pendaftaran tidak ditemukan"
                )

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "text/html; charset=utf-8"
            )
            self.end_headers()

            self.wfile.write(isi.encode("utf-8"))

        except Exception as error:
            print("ERROR STATUS:", error)
            self.send_error(500, "Gagal membuka status")


    def bukaAdmin(self):

        lokasi = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "template",
            "admin.html"
        )

        try:
            with open(lokasi, "r", encoding="utf-8") as file:
                isi = file.read()

            tabel = ""

            if len(dataPendaftar) == 0:

                tabel = """
                <tr>
                    <td colspan="10" class="kosong">
                        Belum ada data pendaftar.
                    </td>
                </tr>
                """

            else:

                nomor = 1

                for data in dataPendaftar:

                    status = data["status"]

                    if status == "Menunggu Verifikasi":
                        classStatus = "menunggu"
                    elif status == "Diterima":
                        classStatus = "diterima"
                    else:
                        classStatus = "ditolak"

                    if status == "Menunggu Verifikasi":

                        aksi = f"""
                        <a href="/terima?nomor={data['nomorPendaftaran']}"
                           class="btn terima">
                            Terima
                        </a>

                        <a href="/tolak?nomor={data['nomorPendaftaran']}"
                           class="btn tolak">
                            Tolak
                        </a>
                        """

                    else:
                        aksi = "-"

                    tabel += f"""
                    <tr>
                        <td>{nomor}</td>
                        <td>{data["nomorPendaftaran"]}</td>
                        <td>{data["nama"]}</td>
                        <td>{data["alamat"]}</td>
                        <td>{data["nomorTelepon"]}</td>
                        <td>{data["asalSekolah"]}</td>
                        <td>{data["namaWali"]}</td>
                        <td>{data["tanggal"]}</td>

                        <td>
                            <span class="status {classStatus}">
                                {status}
                            </span>
                        </td>

                        <td>{aksi}</td>
                    </tr>
                    """

                    nomor += 1

            isi = isi.replace("{{DATA_PENDAFTAR}}", tabel)

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "text/html; charset=utf-8"
            )
            self.end_headers()

            self.wfile.write(isi.encode("utf-8"))

        except Exception as error:
            print("ERROR ADMIN:", error)
            self.send_error(
                500,
                "Gagal membuka halaman admin"
            )


server = HTTPServer(
    ("localhost", 8080),
    ServerWeb
)

print("Server Gontor Registration")
print("Server berjalan di http://localhost:8080")

server.serve_forever()