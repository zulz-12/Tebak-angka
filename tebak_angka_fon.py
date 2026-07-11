import random
import time
import os

number = random.randint(1, 10)
guess = input("tebak angka dari 1 sampi 10: ")

try:
    guess = int(guess)
except ValueError:
    print("Sila masukkan nombor sahaja!")
    exit()

if guess == number:
    print("selamat anda menang")
else:
    # prank shutdown palsu - bukan shutdown betul
    os.system('clear')  # kosongkan skrin
    print("Shutting down...")
    time.sleep(1)
    print("Saving system state...")
    time.sleep(1)
    print("Powering off...")
    time.sleep(2)
    os.system('clear')
    print()  # skrin kosong macam telefon dah mati
