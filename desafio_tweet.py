LIMITE = 140
T = (input("Digite seu Texto..: "))
nume_caracteres = len(T)

if nume_caracteres <= LIMITE:
    print("TWEET")
elif nume_caracteres > LIMITE:
    print("MUTE")