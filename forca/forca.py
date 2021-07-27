import unicodedata, getpass, os

# *********************************************************************
#
#           Funções que serão usadas pelo programa principal
#
# **********************************************************************

# Desenha a forca de acordo com a quantidade de erros, juntamente com a palavra oculta (espaços e letras certas) e a lista de letras já ditas.
def desenhaForca(erros: int, palavra: list, letrasTentadas: list):
    if erros == 0:
        print("______  ")
        print("|    |  ")
        print("|       ")
        print("|       "+"\t"+" ".join(palavra))
        print("|       ")
        print("|       ")
        print("+~~~~~~~+")
    elif erros == 1:
        print("______  ")
        print("|    |  ")
        print("|    O  ")
        print("|       "+"\t"+" ".join(palavra))
        print("|       ")
        print("|       ")
        print("+~~~~~~~+")
    elif erros == 2:
        print("______  ")
        print("|    |  ")
        print("|    O  ")
        print("|    |  "+"\t"+" ".join(palavra))
        print("|    |  ")
        print("|       ")
        print("+~~~~~~~+")
    elif erros == 3:
        print("______  ")
        print("|    |  ")
        print("|    O  ")
        print("|   /|  "+"\t"+" ".join(palavra))
        print("|    |  ")
        print("|       ")
        print("+~~~~~~~+")
    elif erros == 4:
        print("______  ")
        print("|    |  ")
        print("|    O  ")
        print("|   /|\\  "+"\t"+" ".join(palavra))
        print("|    |  ")
        print("|       ")
        print("+~~~~~~~+")
    elif erros == 5:
        print("______  ")
        print("|    |  ")
        print("|    O  ")
        print("|   /|\\  "+"\t"+" ".join(palavra))
        print("|    |  ")
        print("|   /   ")
        print("+~~~~~~~+")
    elif erros == 6:
        print("______  ")
        print("|    |  ")
        print("|    O  ")
        print("|   /|\\  "+"\t"+" ".join(palavra))
        print("|    |  ")
        print("|   / \\  ")
        print("+~~~~~~~+")
    elif erros == 7:
        print("______  ")
        print("|    |  ")
        print("|    @  ")
        print("|   /|\\  "+"\t"+" ".join(palavra))
        print("|    |  ")
        print("|   / \\  ")
        print("+~~~~~~~+")
    print("Letras já ditas:", end=" ")
    for letra in letrasTentadas:
        print(letra, end=" ")

# Para cada letra certa dita pelo jogador, insere todas as ocorrências da mesma no diagrama da palavra oculta impressa jutamente com a forca.
def insereLetraCorreta(letra: str, palavra: str, palavraOculta: list) -> list:
    while letra in palavra:
        i = palavra.find(letra)
        palavraOculta[i] = letra
        palavra = palavra.replace(letra, " ", 1)
    return palavraOculta

# Pede uma letra do alfabeto. Aceita apenas letras do alfabeto com possíveis acentuações em português. Se o usuário digitar mais de um caracter ou um carracter inválido, o programa irá pedir uma letra novamente.
def pedeLetra() -> str:
    letra = input("\nEscolha uma letra do alfabeto: ")
    while not validaLetra(letra):
        if len(letra) > 1:
            letra = input("\nDigite uma única letra do alfabeto: ")
        elif ord(letra) not in letrasValidas():
            letra = input("\nDigite uma letra do alfabeto: ")
    return padronizaString(letra)

# Define uma lista de "letras" válidas.
def letrasValidas() -> list:
    asciiValidos = [x for x in range(65, 91)]
    asciiValidos.extend([x for x in range(97, 123)])
    acentuadas = [128, 129, 130, 131, 135, 136, 144, 147, 154, 160, 161, 162, 163, 181, 182, 183, 198, 199, 210, 214, 224, 226, 228, 229, 233]
    asciiValidos.extend(acentuadas)
    return asciiValidos

# Valida se um caractere inserido é uma letra válida.
def validaLetra(letra: str) -> bool:
    if len(letra) > 1:
        return False
    elif ord(letra) not in letrasValidas():
        return False
    return True

# Pede um palpite da palavra oculta caso o jogador.
def pedePalpite() -> str:
    return padronizaString(input("\nDiga qual é o seu palpite: "))

# Mostra o menu de opções e o retorna como uma lista. As opcoes disponíveis dependem da quantidade de erros e se a dica já foi mostrada.
def mostraOpcoes(dica: bool) -> list:
    if dica:
        menu = [
            "\t1 - Escolher uma letra.",
            "\t2 - Dizer qual é a palavra.",
            "\t3 - Sair.",
            "\t4 - Mostrar dica."
        ]
    else:
        menu = [
            "\t1 - Escolher uma letra.",
            "\t2 - Dizer qual é a palavra.",
            "\t3 - Sair."
        ]
    print("\n\nMenu de Opções:")
    for opcao in menu:
        print(opcao)

# Pede uma das opções do menu.
def pedeOpcao(dica: bool) -> str:
    opcoes = ["1", "2", "3"]
    if dica:
        opcoes.append("4")
    opcao = input("\nDigite o número da opção desejada: ")
    while opcao not in opcoes:
        opcao = input("\nDigite o número da opção desejada: ")
    return opcao
    

def cabecalhoJogador(mensagem: str):
    for x in range(72):
        print("*", end="")
    print("\n\n\t\t" + mensagem + "\n")
    for x in range(72):
        print("*", end="")

# Padroniza uma string para maiúsculas sem acentuação e sem espaços no início ou fim da mesma.
def padronizaString(string: str) -> str:
    return unicodedata.normalize("NFD", string).encode("ascii", "ignore").decode("utf-8").upper().strip()

# Confere se o palpite do jogador está correto.
def conferePalpite(palpite: str, palavra: str) -> bool:
    if palpite == palavra:
        return True
    else:
        return False

# Pergunta se deseja jogar novamente.
def perguntaPorReinicio() -> bool:
    reinicio = ""
    while reinicio not in ["S", "N"]:
        reinicio = padronizaString(input("\nDeseja jogar novamente? (S ou N): "))
    if reinicio == "S":
        return True
    return False

# **********************************************************************
#
#           Programa Principal que roda o Jogo da Forca
#
# **********************************************************************

start = True
while start:
    cabecalhoJogador("Jogador 1")
    palavra = pedePalavraOculta()
    # palavra = padronizaString(getpass.getpass(prompt="\nEscolha uma palavra para ser advinhada: "))
    palavraOculta = ["_" for letra in palavra]
    dica = pedePalavraOculta
    # dica = padronizaString(getpass.getpass(prompt="\nEntre com uma dica para a palavra: "))
    os.system('clear')
    cabecalhoJogador()
    
    letrasTentadas = []
    erros = 0
    terminaJogo = False
    mostraDica = False
    menuComDica = True
    desenhaForca(erros, palavraOculta, letrasTentadas)
    
    while not terminaJogo:
        mostraOpcoes(menuComDica)    
        opcao = pedeOpcao(menuComDica)
    
        if opcao == "1":
            letra = pedeLetra()
            while letra in letrasTentadas:
                print("\nEssa letra já foi usada.")
                letra = pedeLetra()
            letrasTentadas.append(letra)

            os.system('clear')
            if letra in palavra:
                insereLetraCorreta(letra, palavra, palavraOculta)
                if palavraOculta.count("_") == 0:
                    print("\nParabéns, você acertou todas as letras da palavra.")
                    terminaJogo = True
            else:
                erros += 1
                if erros == 7:
                    print("\nTentativas esgotadas. Infelizmente o boneco foi enforcado.")
                    terminaJogo = True
    
        elif opcao == "2":
            palpite = pedePalpite()
            os.system('clear')
            if conferePalpite(palpite, palavra):
                palavraOculta = list(palavra)
                print("\nParabéns, você advinhou a palavra.")
                terminaJogo = True
            else:
                erros += 1
                print(f"\n{palpite} não é palavra correta!")

                if erros == 7:
                    print("\nTentativas esgotadas. Infelizmente o boneco foi enforcado.")
                    terminaJogo = True

        elif opcao == "3":
            terminaJogo = True
            os.system('clear')
            continue

        elif opcao == "4":
            mostraDica = True
            menuComDica = False
            erros += 1
            os.system('clear')

        desenhaForca(erros, palavraOculta, letrasTentadas)
        if mostraDica:
            print("\nDica: "+dica)
        
        if erros == 6:
            menuComDica = False
    
    reinicio = perguntaPorReinicio()
    if not reinicio:
        start = False
                    
    os.system('clear')
