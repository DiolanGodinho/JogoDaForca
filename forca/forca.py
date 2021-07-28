import unicodedata, getpass, os, random
# *********************************************************************
#
#                       Definição de Constantes
#
# **********************************************************************

MAXIMO_DE_ERROS = 7
MODOS_DE_JOGO = [
        "\t1 - Individual.",
        "\t2 - Duelo (1 x 1)"
        ]
OPCOES_DE_JOGADAS = [
        "\t1 - Escolher uma letra.",
        "\t2 - Dizer qual é a palavra.",
        "\t3 - Sair da partida.",
        "\t4 - Mostrar dica."
        ]
BANCO_DE_PALAVRAS = "palavrasComDicas.txt"
MSG_MODOS_JOGO = "\nModos de jogo:"
MSG_OPCOES_JOGADAS = "\nOpções de jogadas:"
MSG_COMPLETOU_PALAVRA = "\nParabéns, você acertou todas as letras da palavra."
MSG_ESGOTOU_TENTATIVAS = "\nTentativas esgotadas. Infelizmente o boneco foi enforcado."
MSG_ADVINHOU_PALAVRA = "\nParabéns, você advinhou a palavra."

# *********************************************************************
#
#           Funções que serão usadas pelo programa principal
#
# **********************************************************************

# Pede ao usuário para selecionar o modo de jogo: individual ou duelo.
def selecionaPalavraEDica(modo: str) -> list:
    if modo == "1":
        return palavraEDicaDoUsuario()
    elif modo == "2":
        return palavraEDicaDoBanco()
        
# Solicita ao jogador uma palavra a ser advinhada e uma dica.
def palavraEDicaDoUsuario() -> list:
    palavra = pedePalavraSemMostraLa("\nEscolha uma palavra para ser advinhada: ")
    dica = pedePalavraSemMostraLa("\nEntre com uma dica para a palavra: ")
    return [palavra, dica]

# Seleciona uma palavra com a respectiva dica do banco de palavras.
def palavraEDicaDoBanco() -> list:
    conteudoDoBanco = pegaConteudoDeArquivo(BANCO_DE_PALAVRAS)
    linhasDoBanco = separaConteudoEmLinhas(conteudoDoBanco)
    palavrasEDicas = separaFrasesPorPalavras(linhasDoBanco)
    return sorteiaItem(palavrasEDicas)

# Retorna o conteudo de um arquivo
def pegaConteudoDeArquivo(caminho: str) -> str:
    arquivo = open("palavrasComDicas", mode="r", encoding="utf-8")
    conteudoDoArquivo = arquivo.read()
    arquivo.close()
    return conteudoDoArquivo

# Separa o conteudo de um arquivo de acordo com as linhas do mesmo.
def separaConteudoEmLinhas(conteudo: str) -> list:
    return conteudo.split("\n")

# Para cada "frase" de uma lista de frases, separa-a por palavras e retorna uma lista com as listas de palavras.
def separaFrasesPorPalavras(linhas: list) -> list:
    return [linha.split() for linha in linhas]

# Seleciona aleatoriamente um item de uma lista
def sorteiaItem(itens: list) -> list:
    return random.choice(itens)

# Retorna a entrada de uma palavra ou frase pelo usuário sem mostrá-la no prompt.
def pedePalavraSemMostraLa(mensagem: str) -> str:
    return padronizaString(getpass.getpass(prompt=mensagem))

# Retorna a entrada de uma palavra ou frase pelo usuário mostrando-a no prompt.
def pedePalavra(mensagem: str) -> str:
    return padronizaString(input(mensagem))

# Padroniza uma string para maiúsculas sem acentuação e sem espaços no início ou fim da mesma.
def padronizaString(string: str) -> str:
    return unicodedata.normalize("NFD", string).encode("ascii", "ignore").decode("utf-8").upper().strip()

# Cria e retorna uma lista de underlines: um para cada letra da palavra a ser advinhada.
def geraEspacosParaLetras(palavra: str) -> list:
    return ["_" for letra in palavra if letra != " " else " "]

# Imprime o diagrama com a forca, a palavra oculta, as letras já tentadas e a dica.
def imprimeDiagrama(erros: int, palavra: list, letras: list, dica: bool):
    desenhaForca(erros, palavra)
    imprimeItensDeLista(letras, "Letras já ditas:", " ")
    if dica:
        print("\nDica: "+dica)

# Desenha a forca de acordo com a quantidade de erros, juntamente com a palavra oculta (espaços e letras certas) e a lista de letras já ditas.
def desenhaForca(erros: int, palavra: list):
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
    
# Imprime uma mesagem a ser passada e os itens de uma lista.
def imprimeItensDeLista(lista: list, mensagem: str, fim="\n": str):
    print(mensagem, end=fim)
    for item in lista:
        print(item, end=fim)

# Define o menu de opções e o retorna como uma lista. As opcoes disponíveis dependem da quantidade de erros e se a dica já foi mostrada.
def defineOpcoesDeJogadas(dica: bool) -> list:
    if dica:
        OPCOES_DE_JOGADAS.pop()
    return menu

# Pede uma das opções do menu.
def pedeOpcao(menu: list) -> str:
    opcao = input("\nDigite o número da opção desejada: ")
    while opcao not in [str(i) for i in range(1, len(menu) + 1)]:
        opcao = input("\nDigite o número da opção desejada: ")
    return opcao

# Pede uma letra do alfabeto. Aceita apenas letras do alfabeto com possíveis acentuações em português. Se o usuário digitar mais de um caracter ou um carracter inválido, o programa irá pedir uma letra novamente.
def pedeLetraValida(tentadas: list) -> str:
    letra = input("\nEscolha uma letra do alfabeto: ")
    while not LetraValida(letra):
        if len(letra) > 1:
            letra = input("\nDigite uma única letra do alfabeto: ")
        elif ord(letra) not in letrasDoPortugues():
            letra = input("\nDigite uma letra do alfabeto: ")
        elif letra in tentadas:
            letra = input("\nEssa letra já foi usada.")
    return padronizaString(letra)

# Valida se um caractere inserido é uma letra válida.
def LetraValida(letra: str, tentadas: list) -> bool:
    if len(letra) > 1 or ord(letra) not in letrasDoPortugues() or letra in tentadas:
        return False
    return True

# Define uma lista de "letras" válidas no Português.
def letrasDoPortugues() -> list:
    asciiPortugues = [x for x in range(65, 91)]
    asciiPortugues.extend([x for x in range(97, 123)])
    acentuadas = [128, 129, 130, 131, 135, 136, 144, 147, 154, 160, 161, 162, 163, 181, 182, 183, 198, 199, 210, 214, 224, 226, 228, 229, 233]
    asciiPortugues.extend(acentuadas)
    return asciiPortugues

def incluiEmLetrasTentadas(letra: str, tentadas: list) -> list:
    tentadas.append(letra)
    return tentadas

# Para cada letra certa dita pelo jogador, insere todas as ocorrências da mesma no diagrama da palavra oculta impressa jutamente com a forca.
def insereLetraCorreta(letra: str, palavra: str, palavraOculta: list) -> list:
    while letra in palavra:
        i = palavra.find(letra)
        palavraOculta[i] = letra
        palavra = palavra.replace(letra, " ", 1)
    return palavraOculta

# Verifica se todas as letras da palavra foram advinhadas.
def completou(palavra: list) -> bool:
    if palavra.count("_") == 0:
        return True
    return False

# Confere se o palpite do jogador está correto.
def palpiteCerto(palpite: str, palavra: str) -> bool:
    if palpite == palavra:
        return True
    else:
        return False

# Pergunta se deseja jogar novamente.
def perguntaPorReinicio() -> bool:
    resposta = ""
    while resposta not in ["S", "N"]:
        resposta = input("\nDeseja jogar novamente? (S ou N): ").upper()
    if resposta == "N":
        return False
    return True

# **********************************************************************
#
#           Programa Principal que roda o Jogo da Forca
#
# **********************************************************************

start = True
while start:
    # Escolhe o modo de jogo
    imprimeItensDeLista(MODOS_DE_JOGO, MSG_MODOS_JOGO)
    modoEscolhido = pedeOpcao(MODOS_DE_JOGO)

    # Seleciona palavra e dica
    palavraEDicaSelecionadas = selecionaPalavraEDica(modoEscolhido)
    palavra = palavraEDicaSelecionadas[0]
    dica = palavraEDicaSelecionadas[1]
    palavraOculta = geraEspacosParaLetras(palavra)
    os.system('clear')
    
    # Inicializa variaveis para rodar o jogo
    letrasTentadas = []
    erros = 0
    jogando = True
    mostraDica = False
    menuComDica = True
    
    # Inicia partida
    imprimeDiagrama(erros, palavraOculta, letrasTentadas, mostraDica)
    while jogando:
        opcoesDeJogadas = defineOpcoesDeJogadas(mostraDica)
        imprimeItensDeLista(opcoesDeJogadas, MSG_OPCOES_JOGADAS)
        jogadaEscolhida = pedeOpcao(opcoesDeJogadas)

        # Tenta uma letra
        if jogadaEscolhida == "1":
            letra = pedeLetraValida(letrasTentadas)
            incluiEmLetrasTentadas(letra)
            os.system('clear')
            
            if letra in palavra:
                insereLetraCorreta(letra, palavra, palavraOculta)
                if completou(palavraOculta):
                    print(MSG_COMPLETOU_PALAVRA)
                    jogando = False
            else:
                erros += 1
                if erros == MAXIMO_DE_ERROS:
                    print(MSG_ESGOTOU_TENTATIVAS)
                    jogando = False

        # Tenta um palpite
        elif jogadaEscolhida == "2":
            palpite = pedePalavra("\nDiga qual é o seu palpite: ")
            os.system('clear')

            if palpiteCerto(palpite, palavra):
                palavraOculta = list(palavra)
                print(MSG_ADVINHOU_PALAVRA)
                jogando = False
            else:
                erros += 1
                print(f"\n{palpite} não é palavra correta!")

                if erros == MAXIMO_DE_ERROS:
                    print(MSG_ESGOTOU_TENTATIVAS)
                    jogando = False

        # Sai da partida
        elif jogadaEscolhida == "3":
            jogando = False
            os.system('clear')
            continue
        
        # Mostra a dica
        elif jogadaEscolhida == "4":
            mostraDica = True
            menuComDica = False
            erros += 1
            os.system('clear')

        imprimeDiagrama(erros, palavraOculta, letrasTentadas, mostraDica)
        
        # Retira a opcao de pedir do menu se faltar apenas um erro para enforcar o boneco.
        if erros == MAXIMO_DE_ERROS - 1:
            menuComDica = False
    
    jogarNovamente = perguntaPorReinicio()
    if not jogarNovamente:
        start = False
                    
    os.system('clear')
