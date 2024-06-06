def tanding(user_choice, computer_choice):
    hasil = ""
    if user_choice == computer_choice:
        hasil = "seri"
    elif (user_choice == "gunting" and computer_choice == "kertas") or \
    (user_choice == "batu" and computer_choice == "gunting") or \
    (user_choice == "kertas" and computer_choice == "batu"):
        hasil = "menang"
    else:
        hasil = "kalah"

    return hasil