import streamlit as st
st.markdown("""
    <style>
    /* Global App Style */
    .stApp {
        background-color: #dceefd;
        font-family: 'Segoe UI', 'Arial', sans-serif;
        color: #0a1a2f;
    }

    /* Judul utama */
    h1 {
        color: #0d47a1;
        text-align: center;
        font-weight: 700;
        border-bottom: 2px solid #90caf9;
        padding-bottom: 10px;
    }

    /* Subjudul dan label */
    .stMarkdown h2, .stMarkdown h3, label {
        color: #0d47a1 !important;
        font-weight: 600;
    }

    /* Input style */
    input, textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #90caf9 !important;
        border-radius: 8px !important;
        padding: 0.5em !important;
    }

    /* Placeholder */
    ::placeholder {
        color: #6d89aa !important;
    }

    /* Tombol utama */
    button[kind="primary"] {
        background-color: #2196f3;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        box-shadow: 1px 2px 6px rgba(0,0,0,0.2);
        border: none;
        transition: 0.3s ease;
    }

    button[kind="primary"]:hover {
        background-color: #1976d2;
        color: white;
        transform: scale(1.02);
    }

    /* Daftar buku tampil rapi */
    .element-container p {
        background-color: #e3f2fd;
        padding: 8px 12px;
        border-radius: 6px;
        margin-bottom: 6px;
        border-left: 4px solid #2196f3;
    }

    /* Alert dan notifikasi */
    .stAlert {
        border-radius: 8px;
        padding: 10px;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)



# Buku
class Buku:
    def __init__(self, JudulBuku, KodeBuku, Penulis, TahunTerbit, JumlahBuku):
        self.JudulBuku = JudulBuku
        self.KodeBuku = KodeBuku
        self.Penulis = Penulis
        self.TahunTerbit = TahunTerbit
        self.JumlahBuku = JumlahBuku

    def __str__(self):
        return f"Judul Buku: {self.JudulBuku}, Kode Buku: {self.KodeBuku}, Penulis: {self.Penulis}, TahunTerbit: {self.TahunTerbit}, Jumlah Buku: {self.JumlahBuku}"

# Inisialisasi data
if 'Data_Buku' not in st.session_state:
    st.session_state.Data_Buku = []

# Tampilan utama
st.title("📚 Data Buku Perpustakaan")

st.write("### Pilihan Menu:")
st.write("1. Tambah Data")
st.write("2. Lihat Data")
st.write("3. Ubah Data")
st.write("4. Hapus Data")

menu = st.text_input("Masukkan angka menu (1-4):")

# Menu 1 - Tambah
if menu == "1":
    st.subheader("➕ Tambah Buku")
    JudulBuku = st.text_input("Masukkan Judul Buku")
    KodeBuku = st.text_input("Masukkan Kode Buku")
    Penulis = st.text_input("Masukkan Penulis Buku")
    TahunTerbit = st.text_input("Masukkan Tahun Terbit Buku")
    JumlahBuku = st.text_input("Masukkan Jumlah Buku")

    if st.button("Simpan"):
        if JudulBuku and KodeBuku and Penulis and TahunTerbit and JumlahBuku:
            buku = Buku(JudulBuku, KodeBuku, Penulis, TahunTerbit, JumlahBuku)
            st.session_state.Data_Buku.append(buku)
            st.success("✅ Data berhasil ditambahkan.")
        else:
            st.warning("⚠️ Harap isi semua kolom.")

# Menu 2 - Lihat
elif menu == "2":
    st.subheader("📄 Daftar Buku")
    if st.session_state.Data_Buku:
        for i, buku in enumerate(st.session_state.Data_Buku, start=1):
            st.write(f"{i}. {buku}")
    else:
        st.info("Belum ada data.")

# Menu 3 - Ubah
elif menu == "3":
    st.subheader("✏️ Ubah Data Buku")
    data = st.session_state.Data_Buku

    if data:
        index = st.number_input("Masukkan nomor buku yang ingin diubah", min_value=1, max_value=len(data), step=1)
        selected = data[index - 1]

        JudulBaru = st.text_input("Judul Buku", selected.JudulBuku)
        KodeBaru = st.text_input("Kode Buku", selected.KodeBuku)
        PenulisBaru = st.text_input("Penulis", selected.Penulis)
        TahunBaru = st.text_input("Tahun Terbit", selected.TahunTerbit)
        JumlahBaru = st.text_input("Jumlah Buku", selected.JumlahBuku)

        if st.button("Simpan Perubahan"):
            if JudulBaru and KodeBaru and PenulisBaru and TahunBaru and JumlahBaru:
                st.session_state.Data_Buku[index - 1] = Buku(JudulBaru, KodeBaru, PenulisBaru, TahunBaru, JumlahBaru)
                st.success("✅ Data buku berhasil diubah.")
            else:
                st.warning("⚠️ Harap isi semua kolom.")
    else:
        st.info("Belum ada data buku.")

# Menu 4 - Hapus
elif menu == "4":
    st.subheader("🗑️ Hapus Data Buku")

    if st.session_state.Data_Buku:
        index = st.number_input("Masukkan nomor buku yang ingin dihapus", min_value=1, max_value=len(st.session_state.Data_Buku), step=1)

        buku_dihapus = st.session_state.Data_Buku[index - 1]
        st.write(f"Buku yang akan dihapus: {buku_dihapus}")

        if st.button("Hapus"):
            st.session_state.Data_Buku.pop(index - 1)
            st.success(f"✅ Buku '{buku_dihapus.JudulBuku}' berhasil dihapus.")
    else:
        st.info("Belum ada data untuk dihapus.")

# Validasi input menu
elif menu != "":
    st.warning("Masukkan angka 1 - 4 sesuai menu.")
