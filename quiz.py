import random

#Enum de Dificuldade
from enum import Enum
class Dificuldade(Enum):
    FACIL = 1
    MEDIA = 2
    DIFICIL = 3
    ALEATORIO = 4

class Pergunta:
    def __init__(self, codigo, dificuldade, descricao, alternativas) -> None:
        self.codigo = codigo
        self.dificuldade = dificuldade
        self.descricao = descricao
        self.alternativas = alternativas
    
    def exibirPergunta(self):
        print("="*20 + " PERGUNTA " +"="*20)
        print(f'{self.descricao.upper()}')
        pass

    def validarResposta(self, respostaDoUsuario, respostaCorreta):
        if (respostaDoUsuario.lower() == respostaCorreta.lower()):
            print(f'Parabéns, você acertou :) ')
        else:
            print(f'Que pena, você errou :( ')
            
        print('\n')
    
class Alternativa: 
    def __init__(self, descricao, resposta_correta) -> None:
        self.descricao = descricao
        self.resposta_correta = resposta_correta

    def exibirAlternativa(self):
        print(f'Opcao: {self.descricao}')


#Factory para criar as instancias das perguntas, baseado no tipo de quiz fornececido pelo strategy
class PerguntaFactory:
    @staticmethod
    def criarPergunta(dificuldade: Dificuldade, pergunta):
        if dificuldade == Dificuldade.FACIL:
            return Pergunta(pergunta['codigo'], pergunta['dificuldade'], pergunta['descricao'], pergunta['alternativas'])
        elif dificuldade == Dificuldade.MEDIA:
            return Pergunta(pergunta['codigo'], pergunta['dificuldade'], pergunta['descricao'], pergunta['alternativas'])
        elif dificuldade == Dificuldade.DIFICIL:
            return Pergunta(pergunta['codigo'], pergunta['dificuldade'], pergunta['descricao'], pergunta['alternativas'])
        elif dificuldade == Dificuldade.ALEATORIO:
            return Pergunta(pergunta['codigo'], pergunta['dificuldade'], pergunta['descricao'], pergunta['alternativas'])


#Strategy para decidir qual o tipo de quiz será gerado baseado na dificuldade.
class StrategyQuiz:
    def __init__(self, dificuldade: Dificuldade, perguntas) -> None:
        self.dificuldade = dificuldade
        self.perguntas = perguntas
        
    def definirQuiz(self):
        if self.dificuldade == Dificuldade.FACIL:
            self.__definirQuizFacil()
        elif self.dificuldade == Dificuldade.MEDIA:
            self.__definirQuizMedio()
        elif self.dificuldade == Dificuldade.DIFICIL:
            self.__definirQuizDificil()
        elif self.dificuldade == Dificuldade.ALEATORIO:
            self.__definirQuizAleatorio()
            
    #Strategy facil                    
    def __definirQuizFacil(self):
        print("="*50)
        print(" "*10 + " QUIZ FACIL selecionado! " + " "*10)
        print("="*50)
        
        questoesFaceis = []
        
        for pergunta in self.perguntas:
            if(pergunta['dificuldade'] == 'FACIL'):
                questoesFaceis.append(pergunta)
                
        for questaoFacil in questoesFaceis:
            self.__exibirPerguntaAoUsuario(Dificuldade.FACIL, questaoFacil)         
        
    #Strategy medio
    def __definirQuizMedio(self):
        print("="*50)
        print(" "*10 + " QUIZ MEDIO selecionado! " + " "*10)
        print("="*50)
        
        questoesMedias = []
        
        for pergunta in self.perguntas:
            if(pergunta['dificuldade'] == 'MEDIA'):
                questoesMedias.append(pergunta)
                
        for questaoMedia in questoesMedias:
            self.__exibirPerguntaAoUsuario(Dificuldade.MEDIA, questaoMedia)
    
    #Strategy dificil
    def __definirQuizDificil(self):
        print("="*50)
        print(" "*10 + " QUIZ DIFICIL selecionado! " + " "*10)
        print("="*50)
        
        questoesDificies = []
        
        for pergunta in self.perguntas:
            if(pergunta['dificuldade'] == 'DIFICIL'):
                questoesDificies.append(pergunta)
                
        for questaoDificil in questoesDificies:
            self.__exibirPerguntaAoUsuario(Dificuldade.DIFICIL, questaoDificil)
    
    #Strategy aleatorio
    def __definirQuizAleatorio(self):
        print("="*50)
        print(" "*10 + " QUIZ ALEATORIO selecionado! " + " "*10)
        print("="*50)
        
        random.shuffle(self.perguntas)

        indicesAleatorios = []

        for i in range(5):
            randomIndice = random.randint(0, 8) # de (0 a 8), é porque meu json possui ao todo, nove perguntas.
            indicesAleatorios.append(randomIndice)

        for x in range(0, 5):
            self.__exibirPerguntaAoUsuario(Dificuldade.ALEATORIO, self.perguntas[indicesAleatorios[x]])
        
    # Criei este método apenas para evitar código repitido nos métodos acima, já que basicamente, todos irão seguir o mesmo fluxo.
    def __exibirPerguntaAoUsuario(self, dificuldade: Dificuldade, questao):
        perguntaCriada = PerguntaFactory.criarPergunta(dificuldade, questao)
        perguntaCriada.exibirPergunta()
        
        respostaCorreta = ''
        for alternativa in perguntaCriada.alternativas:
            novaAlternativa = Alternativa(alternativa['descricao'], alternativa['resposta_correta'])
            if (novaAlternativa.resposta_correta): respostaCorreta = novaAlternativa.descricao
            novaAlternativa.exibirAlternativa()
        
        usuario_resposta = input('Resposta: ')
        perguntaCriada.validarResposta(usuario_resposta, respostaCorreta)


class Quiz:
    @staticmethod
    def gerarQuiz(dificuldade: Dificuldade, perguntas):
        quiz = StrategyQuiz(dificuldade, perguntas)
        quiz.definirQuiz()      

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