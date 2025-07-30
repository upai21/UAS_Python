import streamlit as st

# Buku
class Buku :
    def __init__(self, JudulBuku, KodeBuku, Penulis, TahunTerbit, JumlahBuku):
        self.JudulBuku = JudulBuku
        self.KodeBuku = Kode Buku
        self.Penulis = Penulis
        self.TahunTerbit = Tahun Terbit
        self.JumlahBuku = Jumlah Buku

    def __str__(self):
        return f"Judul Buku: {self.JudulBuku}, Kode Buku: {self.KodeBuku}, Penulis: {self.Penulis}, TahunTerbit: {self.TahunTerbit}, Jumlah Buku : {self.JumlahBuku}"

# Data disimpan di list session_state
if 'Data_Buku' not in st.session_state:
    st.session_state.data_mahasiswa = []

# Tampilan utama
#format berupa judul/bold
st.title("Data Buku Perpustakaan")

#format peenulisan biasa
st.write("### Pilihan Menu:")
st.write("1. Tambah Data")
st.write("2. Lihat Data")
st.write("3. Ubah Data")
st.write("4. Hapus Data")

menu = st.text_input("Masukkan angka menu (1-4):")

# Fungsi menu
elif menu == "1":
    st.subheader("➕ Tambah Buku")
    JudulBuku = st.text_input("Masukkan Judul Buku")
    KodeBuku = st.text_input("Masukkan Kode Buku")
    Penulis = st.text_input("Masukkan Penulis Buku")
    TahunTerbit = st.text_input("Masukkan Tahun Terbit Buku")
    JumlahBuku = st.text_input("Masukkan Jumlah Buku")
    if st.button("Simpan"):
        if nim and nama:
            mhs = Mahasiswa(nim, nama)
            st.session_state.data_mahasiswa.append(mhs)
            st.success("Data berhasil ditambahkan.")
        else:
            st.warning("Harap isi semua kolom.")
            
if menu == "2":
    st.subheader("📄 Daftar Mahasiswa")
    if st.session_state.data_mahasiswa:
        for i, mhs in enumerate(st.session_state.data_mahasiswa):
            st.write(f"{i+1}. {mhs}")
    else:
        st.info("Belum ada data.")

elif menu == "3":
    st.subheader("✏️ Ubah Mahasiswa")
    data = st.session_state.data_mahasiswa
    

elif menu == "4":
    st.subheader("🗑️ Hapus Mahasiswa")
    

elif menu != "":
    st.warning("Masukkan angka 1 - 4 sesuai menu.")


