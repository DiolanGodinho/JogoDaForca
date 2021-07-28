import unicodedata, getpass, os, random
# *********************************************************************
#
#                       Definição de Constantes
#
# **********************************************************************

MAXIMO_DE_ERROS = 7
MODOS_DE_JOGO = [
        "  1 - Individual.",
        "  2 - Duelo (1 x 1)"
        ]
CAMINHO = "palavrasComDicas.txt"
MSG_MODOS_JOGO = "Modos de jogo:\n"
MSG_OPCOES_JOGADAS = "Opções de jogadas:\n"
MSG_COMPLETOU_PALAVRA = "\nParabéns, você acertou todas as letras da palavra."
MSG_ESGOTOU_TENTATIVAS = "\nTentativas esgotadas. Infelizmente o boneco foi enforcado."
MSG_ADVINHOU_PALAVRA = "\nParabéns, você advinhou a palavra."
MSG_BOAS_VINDAS = """
******************************************************
*                                                    *
*            Bem vindo ao jogo da forca.             *
*                                                    *
******************************************************
"""

# *********************************************************************
#
#           Funções que serão usadas pelo programa principal
#
# **********************************************************************

# Imprime uma mesagem a ser passada e os itens de uma lista.
def imprimeItensDeLista(lista: list, mensagem: str, fim="\n"):
    print(mensagem, end=fim)
    for item in lista:
        print(item, end=fim)

# Pede uma das opções do menu.
def pedeOpcao(menu: list) -> str:
    opcao = input("\nDigite o número da opção desejada: ")
    while opcao not in [str(i) for i in range(1, len(menu) + 1)]:
        opcao = input("\nDigite o número da opção desejada: ")
    return opcao

# Pede ao usuário para selecionar o modo de jogo: individual ou duelo.
def selecionaPalavraEDica(modo: str) -> list:
    if modo == "1":
        return palavraEDicaDoBanco()
    elif modo == "2":
        return palavraEDicaDoUsuario()
        
# Seleciona uma palavra com a respectiva dica do banco de palavras.
def palavraEDicaDoBanco() -> list:
    conteudoDoBanco = pegaConteudoDeArquivo(CAMINHO)
    linhasDoBanco = separaConteudoEmLinhas(conteudoDoBanco)
    palavrasEDicas = separaFrasesPorPalavras(linhasDoBanco)
    palavraSorteada = sorteiaItem(palavrasEDicas)
    return [padronizaString(item) for item in palavraSorteada]

# Retorna o conteudo de um arquivo
def pegaConteudoDeArquivo(caminho: str) -> str:
    arquivo = open(caminho, mode="r", encoding="utf-8")
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

# Padroniza uma string para maiúsculas sem acentuação e sem espaços no início ou fim da mesma.
def padronizaString(string: str) -> str:
    return unicodedata.normalize("NFD", string).encode("ascii", "ignore").decode("utf-8").upper().strip()

# Solicita ao jogador uma palavra a ser advinhada e uma dica.
def palavraEDicaDoUsuario() -> list:
    palavra = pedePalavraSemMostraLa("\nEscolha uma palavra para ser advinhada: ")
    dica = pedePalavraSemMostraLa("\nEntre com uma dica para a palavra: ")
    return [palavra, dica]

# Retorna a entrada de uma palavra ou frase pelo usuário sem mostrá-la no prompt.
def pedePalavraSemMostraLa(mensagem: str) -> str:
    return padronizaString(getpass.getpass(prompt=mensagem))

# Cria e retorna uma lista de underlines: um para cada letra da palavra a ser advinhada.
def geraEspacosParaLetras(palavra: str) -> list:
    return ["_" if letra != " " else " " for letra in palavra]

# Imprime o diagrama com a forca, a palavra oculta, as letras já tentadas e a dica.
def imprimeDiagrama(erros: int, palavra: list, letras: list, mostrar: bool, dica: str):
    desenhaForca(erros, palavra)
    imprimeItensDeLista(letras, "\nLetras já ditas:", " ")
    if mostrar:
        print("\n\nDica: "+dica+"\n")
    else:
        print("\n")
    print("*************************************************************\n")

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
    
# Define o menu de opções e o retorna como uma lista. As opcoes disponíveis dependem da quantidade de erros e se a dica já foi mostrada.
def defineOpcoesDeJogadas(dica: bool) -> list:
    OpcoesDejogadas = [
        "  1 - Escolher uma letra.",
        "  2 - Dizer qual é a palavra.",
        "  3 - Sair da partida.",
        "  4 - Mostrar dica."
        ]
    if dica:
        OpcoesDejogadas.pop()
    return OpcoesDejogadas

# Pede uma letra do alfabeto. Aceita apenas letras do alfabeto com possíveis acentuações em português. Se o usuário digitar mais de um caracter ou um carracter inválido, o programa irá pedir uma letra novamente.
def pedeLetraValida(tentadas: list) -> str:
    letra = input("\nEscolha uma letra do alfabeto: ")
    while not LetraValida(letra, tentadas):
        if len(letra) > 1:
            letra = input("\nDigite uma única letra do alfabeto: ")
        elif ord(letra) not in letrasDoPortugues():
            letra = input("\nDigite uma letra do alfabeto: ")
        elif padronizaString(letra) in tentadas:
            letra = input("\nEntre com uma letra não utilizada: ")
    return padronizaString(letra)

# Valida se um caractere inserido é uma letra válida.
def LetraValida(letra: str, tentadas: list) -> bool:
    if (len(letra) > 1) or (ord(letra) not in letrasDoPortugues()) or (padronizaString(letra) in tentadas):
        return False
    return True

# Define uma lista de "letras" válidas no Português.
def letrasDoPortugues() -> list:
    asciiPortugues = [x for x in range(65, 91)]
    asciiPortugues.extend([x for x in range(97, 123)])
    acentuadas = [128, 129, 130, 131, 135, 136, 144, 147, 154, 160, 161, 162, 163, 181, 182, 183, 198, 199, 210, 214, 224, 226, 228, 229, 233]
    asciiPortugues.extend(acentuadas)
    return asciiPortugues

def incluiItemEmLista(letra: str, tentadas: list) -> list:
    if letra not in tentadas:
        tentadas.append(letra)
    return tentadas

# Para cada letra certa dita pelo jogador, insere todas as ocorrências da mesma no diagrama da palavra oculta impressa jutamente com a forca.
def insereLetraCorreta(letra: str, palavra: str, palavraOculta: list) -> list:
    while letra in palavra:
        i = palavra.find(letra)
        palavraOculta[i] = letra
        palavra = palavra.replace(letra, " ", 1)
    return palavraOculta

# Imprime mesagem, caso a letra não ocorra na palavra.
def mostraMensagemDeLetraIncorreta(letra: str, palavra: str):
    ocorrencias = palavra.count(letra)
    if ocorrencias == 0:
        print(f"\nA palavra não possui a letra {letra}.")
    
# Verifica se todas as letras da palavra foram advinhadas.
def completou(palavra: list) -> bool:
    if palavra.count("_") == 0:
        return True
    return False

# Retorna a entrada de uma palavra ou frase pelo usuário mostrando-a no prompt.
def pedePalavra(mensagem: str) -> str:
    return padronizaString(input(mensagem))

# Confere se o palpite do jogador está correto.
def palpiteCerto(palpite: str, palavra: str) -> bool:
    if palpite == palavra:
        return True
    else:
        return False

# Retorna uma lista com as letras da palavra.
def desvendaPalavra(palavra: str) -> list:
    return list(palavra)

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
    print(MSG_BOAS_VINDAS)
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
    imprimeDiagrama(erros, palavraOculta, letrasTentadas, mostraDica, dica)
    while jogando:
        opcoesDeJogadas = defineOpcoesDeJogadas(mostraDica)
        imprimeItensDeLista(opcoesDeJogadas, MSG_OPCOES_JOGADAS)
        jogadaEscolhida = pedeOpcao(opcoesDeJogadas)

        # Tenta uma letra
        if jogadaEscolhida == "1":
            letra = pedeLetraValida(letrasTentadas)
            incluiItemEmLista(letra, letrasTentadas)
            os.system('clear')
            
            if letra in palavra:
                insereLetraCorreta(letra, palavra, palavraOculta)
                if completou(palavraOculta):
                    print(MSG_COMPLETOU_PALAVRA)
                    jogando = False
            else:
                erros += 1
                mostraMensagemDeLetraIncorreta(letra, palavra)

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

        # Enforca o boneco
        if erros == MAXIMO_DE_ERROS:
            print(MSG_ESGOTOU_TENTATIVAS)
            palavraOculta = desvendaPalavra(palavra)
            jogando = False

        imprimeDiagrama(erros, palavraOculta, letrasTentadas, mostraDica, dica)
        
        # Retira a opcao de pedir do menu se faltar apenas um erro para enforcar o boneco.
        if erros == MAXIMO_DE_ERROS - 1:
            menuComDica = False
    
    jogarNovamente = perguntaPorReinicio()
    if not jogarNovamente:
        start = False
                    
    os.system('clear')
