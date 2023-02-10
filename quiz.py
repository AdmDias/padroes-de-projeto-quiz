import random

from enum import Enum
class Dificuldade(Enum):
    FACIL = 1
    MEDIA = 2
    DIFICIL = 3
    ALEATORIO = 4

class Pergunta:
    def __init__(self, codigo, descricao, alternativas) -> None:
        self.codigo = codigo
        self.descricao = descricao
        self.alternativas = alternativas
    
    def exibirPergunta(self):
        pass

    def validarResposta(self, respostaCorreta, respostaDoUsuario):
        if (respostaCorreta.lower() == respostaDoUsuario.lower()): print(f'Parabéns, você acertou :) ')
        else: print(f'Que pena, você errou :( ')
        print('\n')
    
class Alternativa: 
    def __init__(self, descricao, resposta_correta) -> None:
        self.descricao = descricao
        self.resposta_correta = resposta_correta

    def exibirAlternativa(self):
        print(f'Opcao: {self.descricao}')

class PerguntaFacil(Pergunta):
    pass

class PerguntaMedia(Pergunta):
    pass

class PerguntaDificil(Pergunta):
    pass

class PerguntaAleatoria(Pergunta):
    def exibirPergunta(self):    
        print(f'{self.descricao}')


class PerguntaFactory:
    @staticmethod
    def criarPergunta(dificuldade: Dificuldade, pergunta):
        if dificuldade == dificuldade.FACIL:
            return PerguntaFacil(pergunta['codigo'], pergunta['descricao'], pergunta['alternativas'])
        elif dificuldade == dificuldade.MEDIA:
            return PerguntaMedia(pergunta['codigo'], pergunta['descricao'], pergunta['alternativas'])
        elif dificuldade == dificuldade.DIFICIL:
            return PerguntaDificil(pergunta['codigo'], pergunta['descricao'], pergunta['alternativas'])
        elif dificuldade == dificuldade.ALEATORIO:
            return PerguntaAleatoria(pergunta['codigo'], pergunta['descricao'], pergunta['alternativas'])


class Quiz:
    @staticmethod
    def gerarQuiz(dificuldade: Dificuldade, perguntas):
        if (dificuldade.ALEATORIO):
            print('\n')
            print("="*40)
            print('Quiz aleatorio selecionado!')
            print('\n')

            indicesAleatorios = []

            for indice in range(5):
                randomIndice = random.randint(0, 8)
                indicesAleatorios.append(randomIndice)

            for x in range(0, 5):
                perguntaCriada = PerguntaFactory.criarPergunta(dificuldade.ALEATORIO, perguntas[indicesAleatorios[x]])
                perguntaCriada.exibirPergunta()

                respostaCorreta = ''
                for alternativa in perguntaCriada.alternativas:
                    novaAlternativa = Alternativa(alternativa['descricao'], alternativa['resposta_correta'])
                    if(novaAlternativa.resposta_correta): respostaCorreta = novaAlternativa.descricao
                    novaAlternativa.exibirAlternativa()
                
                cmd_resposta = input('Informe sua resposta: ')
                perguntaCriada.validarResposta(cmd_resposta, respostaCorreta)
            

if __name__ == '__main__':
    import json

    jsonData = json.load(open('db.json'))

    perguntas = jsonData['perguntas']

    print('Bem vindo, escolha a dificuldade do quiz')
    print('1 - Facil')
    print('2 - Medio')
    print('3 - Dificil')
    print('4 - Aleatorio')
    cmd_opcao = input('-> ')

    if (cmd_opcao == '1'):
        Quiz.gerarQuiz(Dificuldade.FACIL, perguntas)
    elif (cmd_opcao == '2'):
        Quiz.gerarQuiz(Dificuldade.MEDIA, perguntas)
    elif (cmd_opcao == '3'):
        Quiz.gerarQuiz(Dificuldade.DIFICIL, perguntas)
    elif (cmd_opcao == '4'):
        Quiz.gerarQuiz(Dificuldade.ALEATORIO, perguntas)