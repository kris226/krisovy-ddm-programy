import os
import sys
sys.set_int_max_str_digits(99999)
os.system("cls")
cislo = int(input ("zadej cislo"))
kroky = 0
while True:
    kroky = kroky + 1

    print(cislo)

    if cislo == 1:
        break

    if cislo % 2 == 0:
        cislo = cislo // 2

    elif cislo % 2 == 1:
        cislo = cislo * 3 + 1



print(f"pocet kroku byl:{kroky}")