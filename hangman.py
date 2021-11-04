# LIBRARY
from random import randint

# TABULEIRO
board = ["""
    _________
    |       |
    |
    |
    |
____|____       """, """
    _________
    |       |
    |       0
    |
    |
____|____       """, """
    _________
    |       |
    |       0
    |       |
    |
____|____       """, """
    _________
    |       |
    |       0
    |      /|
    |
____|____       """, """
    _________
    |       |
    |       0
    |      /|\
    |
____|____       """, """
    _________
    |       |
    |       0
    |      /|\
    |      /
____|____       """, """
    _________
    |       |
    |       0
    |      /|\
    |      / \
____|____       """]

# Classe
class Hangman():

    # Método Construtor
    def __init__(self, word):
        self.word = word.lower()        # RESPOSTA CHAVE
        self.true_letters = []          # LISTA DE LETRAS CERTAS
        self.false_letters = []         # LISTA DE LETRAS ERRADAS

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word and letter not in self.true_letters:
            self.true_letters.append(letter)
        elif letter not in self.word and letter not in self.false_letters:
            self.false_letters.append(letter)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.false_letters) == 6)

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.true_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(f"{board[len(self.false_letters)]}\n")
        print(f"WORD: {self.hide_word()}\n")
        print(f"MISSED LETTERS: {self.false_letters}\n")
        print(f"CORRECT LETTERS: {self.true_letters}\n")

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("words.txt", "rt") as f:
        bank = f.readlines()
    return bank[randint(0, len(bank))].strip()

# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    print('>' * 10 + ' HANGMAN ' + '<' * 10)
    while (game.hangman_won() == False):
        game.print_game_status()
        letter = str(input("What's the letter? "))[0].lower()
        game.guess(letter)
    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nCongratulations! You won!')
    else:
        print('\nGame Over! You lost!')
        print(f'Word: {game.word}')
    print('\nThat was nice. See You later.')

# Executa o programa
if __name__ == "__main__":
    main()
