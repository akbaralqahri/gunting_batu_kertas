import streamlit as st
import random
import tanding
import phaseWin
import phaseLose   

def main():

    # Deklarasi variabel
    user_lives = 5
    user_win = 0
    choice = ["batu", "kertas", "gunting"]

    # Tampilan awal
    st.title("Permainan Gunting, Batu, Kertas")
    st.write("Pilihan Anda: gunting, batu, kertas")

    # Loop permainan
    while True:

        # Fase 1: Pemain menang
        if user_win <= 2 and user_win >= 0:

            # Input pilihan pemain
            user_choice = st.selectbox("Pilihan Anda:", choice)

            # Periksa apakah pilihan pemain valid
            if user_choice not in choice:
                st.write("Pilihan tidak valid. Coba lagi.")
                continue

            # Pilihan komputer
            computer_choice = phaseWin.phase1(user_choice, 0.9)

            # Hasil permainan
            result = tanding.tanding(user_choice, computer_choice)

            # Update nyawa dan skor
            if result == "kalah":
                user_lives -= 1
            elif result == "menang":
                user_win += 1

            # Tampilkan hasil permainan
            st.write(f"Hasil permainan: {result}")
            st.write(f"Pilihan Komputer: {computer_choice}")
            st.write(f"Skor Anda: {user_win}, Nyawa Anda: {user_lives}")

        # Fase 2: Pemain mengejar
        elif user_win > 2 and user_win <= 3 and user_lives > 0:

            # Input pilihan pemain
            user_choice = st.selectbox("Pilihan Anda:", choice)

            # Periksa apakah pilihan pemain valid
            if user_choice not in choice:
                st.write("Pilihan tidak valid. Coba lagi.")
                continue

            # Pilihan komputer
            computer_choice = random.choice(choice)

            # Hasil permainan
            result = tanding.tanding(user_choice, computer_choice)

            # Update nyawa dan skor
            if result == "kalah":
                user_lives -= 1
            elif result == "menang":
                user_win += 1

            # Tampilkan hasil permainan
            st.write(f"Hasil permainan: {result}")
            st.write(f"Pilihan Komputer: {computer_choice}")
            st.write(f"Skor Anda: {user_win}, Nyawa Anda: {user_lives}")

        # Fase 3: Pemain bertahan
        elif user_win >= 4 and user_win < 5 and user_lives > 0:

            # Input pilihan pemain
            user_choice = st.selectbox("Pilihan Anda:", choice)

            # Periksa apakah pilihan pemain valid
            if user_choice not in choice:
                st.write("Pilihan tidak valid. Coba lagi.")
                continue

            # Pilihan komputer
            computer_choice = phaseLose.phase1(user_choice, 0.9)

            # Hasil permainan
            result = tanding.tanding(user_choice, computer_choice)

            # Update nyawa dan skor
            if result == "kalah":
                user_lives -= 1
            elif result == "menang":
                user_win += 1

            # Tampilkan hasil permainan
            st.write(f"Hasil permainan: {result}")
            st.write(f"Pilihan Komputer: {computer_choice}")
            st.write(f"Skor Anda: {user_win}, Nyawa Anda: {user_lives}")

        # Pemain menang
        if user_win == 5:
            st.write("Anda menang!")
            break

        # Pemain kalah
        elif user_lives == 0:
            st.write("Anda kehabisan nyawa. Permainan berakhir.")
            break

if __name__ == "__main__":
    main()