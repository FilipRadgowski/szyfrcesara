import re

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

n = 1
text = "The quick brown fox jumps over the lazy dog"
o = 0

modchar = ''
modtext = ""
cleantext = ""
support = 0
alphalen = len(alphabet)

def cypher():
    global modtext
    for i in cleantext:
        modchar = i

        if modchar != ' ':
            for j in range(alphalen):
                if alphabet[j] == modchar:
                    if (j + n) < len(alphabet):
                        modchar = alphabet[j+n]
                        break
                    else:
                        support = (j + n) - len(alphabet)
                        modchar = alphabet[support]
                        break
        else:
            modchar = ' '
        modtext += modchar

def decypher():
    global modtext
    for i in cleantext:
        modchar = i

        if modchar != ' ':
            for j in range(alphalen):
                if alphabet[j] == modchar:
                    if j + n >= len(alphabet):
                        modchar = alphabet[j-n]
                        break
                    else:
                        support = (j - n) + len(alphabet)
                        modchar = alphabet[support]
                        break
        else:
            modchar = ' '
        modtext += modchar

n = int(input("Podaj przesunięcie: "))
text = input("Podaj tekst: ")
o = int(input("Wybierz tryb. 0 - szyfrowanie, 1 - deszyfrowanie: "))

cleantext = re.sub('/[^a-zA-Z0-9 ]/g', '', text)

if o == 0:
    print("Szyfrowanie...\n")
    cypher()
    print("Przesunięcie:", n)
    print("Tekst jawny:", text)
    print("Tekst zaszyfrowany:", modtext)

elif o == 1:
    print("Deszyfrowanie...\n")
    decypher()
    print("Przesunięcie:", n)
    print("Tekst deszyfrowany:", text)
    print("Tekst rozszyfrowany:", modtext)

else:
    print ("\nPodano nieprawidłowy tryb.")