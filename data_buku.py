import streamlit as st

# Buku
class Buku :
    def __init__(self, JudulBuku, KodeBuku, Penulis, TahunTerbit, JumlahBuku):
        self.JudulBuku = JudulBuku
        self.KodeBuku = KodeBuku
        self.Penulis = Penulis
        self.TahunTerbit = TahunTerbit
        self.JumlahBuku = JumlahBuku

    def __str__(self):
        return f"Judul Buku: {self.JudulBuku}, Kode Buku: {self.KodeBuku}, Penulis: {self.Penulis}, TahunTerbit: {self.TahunTerbit}, Jumlah Buku : {self.JumlahBuku}"

# Data disimpan di list session_state
if 'Data_Buku' not in st.session_state:
    st.session_state.Data_Buku = []

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
if menu == "1":
    st.subheader("➕ Tambah Buku 🤙🤪🫳")
    JudulBuku = st.text_input("Masukkan Judul Buku")
    KodeBuku = st.text_input("Masukkan Kode Buku")
    Penulis = st.text_input("Masukkan Penulis Buku")
    TahunTerbit = st.text_input("Masukkan Tahun Terbit Buku")
    JumlahBuku = st.text_input("Masukkan Jumlah Buku")
    if st.button("Simpan"):
        if  JudulBuku and KodeBuku and Penulis and TahunTerbit and JumlahBuku:
            buku = Buku (JudulBuku, KodeBuku, Penulis, TahunTerbit, JumlahBuku)
            st.session_state.Data_Buku.append(buku)
            st.success("Data berhasil ditambahkan.")
        else:
            st.warning("Harap isi semua kolom.")
            
elif menu == "2":
    st.subheader("📄 Daftar Buku")
    if st.session_state.Data_Buku:
        for i, buku in enumerate(st.session_state.Data_Buku):
            st.write(f"{i+1}. {buku}")
    else:
        st.info("Belum ada data.")

elif menu == "3":
    st.subheader("✏️ Ubah Data Buku")

    if st.session_state.Data_Buku:
        index = st.number_input("Pilih indeks buku yang ingin diubah (mulai dari 0)", min_value=0, max_value=len(st.session_state.Data_Buku)-1, step=1)
        buku = st.session_state.Data_Buku[index]

        JudulBaru = st.text_input("Judul Buku", value=buku.JudulBuku)
        KodeBaru = st.text_input("Kode Buku", value=buku.KodeBuku)
        PenulisBaru = st.text_input("Penulis", value=buku.Penulis)
        TahunBaru = st.text_input("Tahun Terbit", value=buku.TahunTerbit)
        JumlahBaru = st.text_input("Jumlah Buku", value=buku.JumlahBuku)

        if st.button("Simpan Perubahan"):
            buku.JudulBuku = JudulBaru
            buku.KodeBuku = KodeBaru
            buku.Penulis = PenulisBaru
            buku.TahunTerbit = TahunBaru
            buku.JumlahBuku = JumlahBaru
            st.success("Data buku berhasil diperbarui.")
    else:
        st.info("Belum ada data untuk diubah.")

elif menu == "4":
    st.subheader("🗑️ Hapus Data Buku")

    if st.session_state.Data_Buku:
        index = st.number_input("Pilih indeks buku yang ingin dihapus (mulai dari 0)", min_value=0, max_value=len(st.session_state.Data_Buku)-1, step=1)

        if st.button("Hapus"):
            buku_dihapus = st.session_state.Data_Buku.pop(index)
            st.success(f"Buku '{buku_dihapus.JudulBuku}' berhasil dihapus.")
    else:
        st.info("Belum ada data untuk dihapus.")


