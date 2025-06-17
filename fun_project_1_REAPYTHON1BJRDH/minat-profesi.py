import streamlit as st

st.title("Mini Quiz Talent Mapping")
st.write("Quiz ini bertujuan untuk menentukan profesi yang potensial untuk kamu berdasarkan minat")

st.write("""
Sebelum mulai quiz, baca petunjuknya dulu yuk!
1. Pilihlah salah satu jawaban di setiap nomor. Setiap nomor wajib diisi dan jawaban yang diberikan harus menggambarkan minat yang Kamu miliki  
2. Kalo udah jawab semua pertanyaan, klik tombol "Submit" yaa  
3. Get Ready..! Rekomendasi profesi Kamu akan muncul
""")

# Inisialisasi session_state
if "mulai_quiz" not in st.session_state:
    st.session_state.mulai_quiz = False
if "submit_quiz" not in st.session_state:
    st.session_state.submit_quiz = False

# Tombol mulai quiz
if st.button("Mulai Quiz"):
    st.session_state.mulai_quiz = True

# Tampilkan form hanya jika quiz dimulai dan belum disubmit
if st.session_state.mulai_quiz:
    nama = st.text_input("Nama: ", disabled=st.session_state.submit_quiz)
    with st.form("quiz_form"):
        p1 = st.radio("1. Kamu paling suka belajar apa nih?",
                      ["Algoritma dan Pemrograman", "Statistika", "Ekonomi"],
                      index= None, disabled= st.session_state.submit_quiz)
        p2 = st.radio("2. Software apa yang sering kamu gunakan?",
                      ["VS Code", "R", "E-Views"], index= None,
                      disabled= st.session_state.submit_quiz)
        p3 = st.radio("3. Kalo lagi ada waktu luang, apa yang paling kamu suka lakukan?",
                      ["Belajar ngoding", "Menganalisis data", "Liatin grafik saham"],
                      index=None, disabled= st.session_state.submit_quiz)
        submitted = st.form_submit_button("Submit")

    if submitted:
        if not (nama and p1 and p2 and p3):
            st.audio("assets/salah.mp3", format="audio/mpeg", autoplay=True, end_time=3,
                     start_time=2.99)
            st.error("Semua pertanyaan harus dijawab!")
        else:
            st.session_state.submit_quiz = True
            st.rerun()

# Jika sudah submit, hitung skor dan tampilkan hasil
if st.session_state.submit_quiz:
    st.audio("assets/jeng-jeng.mp3", format="audio/mpeg", autoplay=True, end_time=1)
    skor = 0
    mapping = {
        "Algoritma dan Pemrograman": 1,
        "Statistika": 2,
        "Ekonomi": 3,
        "VS Code": 1,
        "R": 2,
        "E-Views": 3,
        "Belajar ngoding": 1,
        "Menganalisis data": 2,
        "Liatin grafik saham": 3
    }

    skor += mapping[p1]
    skor += mapping[p2]
    skor += mapping[p3]

    if skor <= 4:
        st.success(f"Selamat {nama}! Kamu cocok jadi Software Engineer")
        st.image("assets/Software Engineer.jpg")
        st.write("""
        Software Engineer adalah profesional yang merancang, membangun, menguji, dan memelihara sistem perangkat lunak.
        """)
    elif skor <= 6:
        st.success(f"Selamat {nama}! Kamu cocok jadi Data Scientist")
        st.image("assets/data scientist.jpeg")
        st.write("""
        Data Scientist adalah ahli yang menganalisis dan menginterpretasikan data kompleks untuk menemukan pola dan wawasan.
        """)
    else:
        st.success(f"Selamat {nama}! Kamu cocok jadi Ekonom")
        st.image("assets/ekonom.png")
        st.write("""
        Ekonom mempelajari cara individu dan pemerintah mengambil keputusan dalam mengelola sumber daya yang terbatas.
        """)

    # Reset quiz
    if st.button("Reset"):
        for key in ["mulai_quiz","submit_quiz"]:
            st.session_state.pop(key, None)
        st.rerun()
