# ==============================================================================
# 1. CLASS KARYAWAN (SUPERCLASS)
# ==============================================================================
class Karyawan:
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float):
        self.nama = nama                  # Public attribute
        self.id_karyawan = id_karyawan    # Public attribute
        self.__gaji_pokok = gaji_pokok    # Private attribute (Encapsulation)

    # Getter untuk mengambil nilai gaji pokok
    @property
    def gaji_pokok(self):
        return self.__gaji_pokok

    # Setter untuk mengubah nilai gaji pokok dengan validasi
    @gaji_pokok.setter
    def gaji_pokok(self, nilai_baru):
        if nilai_baru <= 0:
            print(f"[PERINGATAN] Gaji pokok untuk {self.nama} harus lebih besar dari 0!")
        else:
            self.__gaji_pokok = nilai_baru

    # Method untuk menghitung gaji total dasar
    def hitung_gaji_total(self):
        return self.__gaji_pokok

    # Method untuk menampilkan informasi dasar
    def tampilkan_info(self):
        print(f"Nama         : {self.nama}")
        print(f"ID Karyawan  : {self.id_karyawan}")
        print(f"Gaji Pokok   : Rp{self.__gaji_pokok:,.0f}")


# ==============================================================================
# 2. CLASS KARYAWANTETAP (CHILD CLASS)
# ==============================================================================
class KaryawanTetap(Karyawan):
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float, tunjangan: float):
        # Memanggil constructor superclass
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan        # Public attribute tambahan

    # Overriding method hitung_gaji_total
    def hitung_gaji_total(self):
        return self.gaji_pokok + self.tunjangan

    # Overriding method tampilkan_info
    def tampilkan_info(self):
        print("=== DATA KARYAWAN TETAP ===")
        super().tampilkan_info()          # Menampilkan info dasar dari superclass
        print(f"Tunjangan    : Rp{self.tunjangan:,.0f}")
        print(f"Total Gaji   : Rp{self.hitung_gaji_total():,.0f}")
        print("-" * 30)


# ==============================================================================
# 3. CLASS KARYAWANKONTRAK (CHILD CLASS)
# ==============================================================================
class KaryawanKontrak(Karyawan):
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float, jam_lembur: int, tarif_lembur: float):
        # Memanggil constructor superclass
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.jam_lembur = jam_lembur      # Public attribute tambahan
        self.tarif_lembur = tarif_lembur  # Public attribute tambahan

    # Overriding method hitung_gaji_total
    def hitung_gaji_total(self):
        return self.gaji_pokok + (self.jam_lembur * self.tarif_lembur)

    # Overriding method tampilkan_info
    def tampilkan_info(self):
        print("=== DATA KARYAWAN KONTRAK ===")
        super().tampilkan_info()          # Menampilkan info dasar dari superclass
        print(f"Lembur       : {self.jam_lembur} jam (Tarif: Rp{self.tarif_lembur:,.0f}/jam)")
        print(f"Total Gaji   : Rp{self.hitung_gaji_total():,.0f}")
        print("-" * 30)


# ==============================================================================
# MAIN PROGRAM (KETENTUAN PENGUJIAN KODE)
# ==============================================================================
if __name__ == "__main__":
    # 1. Buat minimal 1 objek KaryawanTetap dan 1 objek KaryawanKontrak
    karyawan1 = KaryawanTetap("rahull", "T001", 5000000, 1500000)
    karyawan2 = KaryawanKontrak("jule", "K002", 3500000, 10, 50000)

    # 2. Simpan kedua objek ke dalam list bernama daftar_karyawan
    daftar_karyawan = [karyawan1, karyawan2]

    # 3. Demonstrasi Polymorphism: Looping untuk memanggil tampilkan_info()
    print("\n--- DEMONSTRASI POLYMORPHISM ---")
    for kry in daftar_karyawan:
        kry.tampilkan_info()

    # 4. Demonstrasi Encapsulation: Ubah gaji dengan nilai tidak valid & valid
    print("\n--- DEMONSTRASI ENCAPSULATION ---")
    
    # Mencoba mengubah gaji dengan nilai tidak valid (<= 0)
    print("Mencoba mengubah gaji jule menjadi Rp-500.000:")
    karyawan1.gaji_pokok = -500000  # Akan memicu peringatan di setter
    
    print("\nMencoba mengubah gaji jule menjadi nilai valid Rp5.500.000:")
    karyawan1.gaji_pokok = 5500000  # Nilai valid, berhasil diubah
    
    # Tampilkan ulang hasilnya untuk membuktikan perubahan data
    print("\nInfo terbaru setelah gaji pokok diperbarui:")
    karyawan1.tampilkan_info()
