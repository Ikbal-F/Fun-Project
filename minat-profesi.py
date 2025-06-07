import streamlit as st

st.title("Mini Quiz Talent Mapping")
st.write("Quiz ini bertujuan untuk menentukan profesi yang potensial untuk kamu berdasarkan minat")

st.write("""
Sebelum mulai quiz, baca petunjuknya dulu yuk!
1. Pilihlah salah satu jawaban di setiap nomor. Setiap nomor wajib diisi dan jawaban yang diberikan harus menggambarkan minat yang Kamu miliki  
2. Kalo udah jawab semua pertanyaan, klik tombol "Submit" yaa  
3. Get Ready..! Rekomendasi profesi Kamu akan muncul
""")

# Inisialisasi sesi agar quiz bisa dimulai dan disubmit
if "mulai_quiz" not in st.session_state:
    st.session_state.mulai_quiz = False
if "submit_quiz" not in st.session_state:
    st.session_state.submit_quiz = False

# Tombol mulai quiz
if st.button("Mulai Quiz"):
    st.session_state.mulai_quiz = True
    st.session_state.submit_quiz = False 

# Jika quiz dimulai, tampilkan pertanyaan
if st.session_state.mulai_quiz:
    p1 = st.radio("1. Kamu paling suka belajar apa nih?", 
                  ["Algoritma dan Pemrograman", "Statistika", "Ekonomi"], key="p1",
                  index=None)
    p2 = st.radio("2. Software apa yang sering kamu gunakan?", 
                  ["VS Code", "R", "E-Views"], key="p2", index=None)
    p3 = st.radio("3. Kalo lagi ada waktu luang, apa yang paling kamu suka lakukan?", 
                  ["Belajar ngoding", "Menganalisis data", "Liatin grafik saham"], key="p3",
                  index=None)

    # Tombol submit
    if st.button("Submit"):
        if not (p1 and p2 and p3):
            st.error("Semua pertanyaan harus dijawab!")
        else:
            st.session_state.submit_quiz = True

# Jika sudah submit, hitung skor dan tampilkan hasil
if st.session_state.submit_quiz:
    skor = 0
    if st.session_state.p1 == "Algoritma dan Pemrograman":
        skor += 1
    elif st.session_state.p1 == "Statistika":
        skor += 2
    else:
        skor += 3

    if st.session_state.p2 == "VS Code":
        skor += 1
    elif st.session_state.p2 == "R":
        skor += 2
    else:
        skor += 3

    if st.session_state.p3 == "Belajar ngoding":
        skor += 1
    elif st.session_state.p3 == "Menganalisis data":
        skor += 2
    else:
        skor += 3

    # Output hasil akhir
    if skor <= 4:
        st.success("Selamat! Kamu cocok jadi Software Engineer!")
    elif skor <= 6:
        st.success("Selamat! Kamu cocok jadi Data Scientist!")
    else:
        st.success("Selamat! Kamu cocok jadi Ekonom!")

    # Reset quiz untuk memulai ulang
    if st.button("Reset"):
        st.session_state.mulai_quiz = False
        st.session_state.submit_quiz = False
        for key in ["p1", "p2", "p3"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()