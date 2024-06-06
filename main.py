import phaseWin
import phaseLose
import tanding
import random

def main():

    print("+----------------------------------------------------+")
    print("+ Selamat datang di permainan Gunting, Batu, Kertas! +")
    print("+----------------------------------------------------+")

    user_lives = 5
    user_win = 0
    choice = ["batu", "kertas", "gunting"]

    while True:
        while user_win <= 2 and user_win >= 0 and user_lives > 0:
            user_choice = input("Masukkan pilihan Anda: ").lower()

            # Periksa apakah pilihan pengguna valid
            if user_choice not in ["gunting", "batu", "kertas"]:
                print("Pilihan tidak valid. Coba lagi.")
                continue

            computer_choice = phaseWin.phase1(user_choice, 0.9)
            hasil = tanding.tanding(user_choice, computer_choice)

            if hasil == "kalah":
                user_lives -= 1
            elif hasil == "menang":
                user_win += 1

            print("+-------------------------------+")
            print(f"| Hasil permainan  :", hasil, "\t|")
            print(f"| Pilihan Komputer : {computer_choice}\t|")
            print(f"| Skor Anda: {user_win}, Nyawa Anda: {user_lives}\t|")
            print("+-------------------------------+")

        while (user_win > 2 and user_win <= 3 and user_lives > 0):

            user_choice = input("Masukkan pilihan Anda: ").lower()

            # Periksa apakah pilihan pengguna valid
            if user_choice not in ["gunting", "batu", "kertas"]:
                print("Pilihan tidak valid. Coba lagi.")
                continue

            computer_choice = random.choice(choice)
            hasil = tanding.tanding(user_choice, computer_choice)

            if hasil == "kalah":
                user_lives -= 1
            elif hasil == "menang":
                user_win += 1

            print("+-------------------------------+")
            print(f"| Hasil permainan  :", hasil, "\t|")
            print(f"| Pilihan Komputer : {computer_choice}\t|")
            print(f"| Skor Anda: {user_win}, Nyawa Anda: {user_lives}\t|")
            print("+-------------------------------+")

        while ((user_win >= 4 and user_win < 5 and user_lives > 0)):

            user_choice = input("Masukkan pilihan Anda: ").lower()

            # Periksa apakah pilihan pengguna valid
            if user_choice not in ["gunting", "batu", "kertas"]:
                print("Pilihan tidak valid. Coba lagi.")
                continue

            computer_choice = phaseLose.phase1(user_choice, 1)
            hasil = tanding.tanding(user_choice, computer_choice)

            if hasil == "kalah":
                user_lives -= 1
            elif hasil == "menang":
                user_win += 1

            print("+-------------------------------+")
            print(f"| Hasil permainan  :", hasil, "\t|")
            print(f"| Pilihan Komputer : {computer_choice}\t|")
            print(f"| Skor Anda: {user_win}, Nyawa Anda: {user_lives}\t|")
            print("+-------------------------------+")

        if user_win == 5:
            print("Anda menang!")
            break
        elif user_lives == 0:
            print("Anda kehabisan nyawa. Permainan berakhir.")
            break

if __name__ == "__main__":
    main()