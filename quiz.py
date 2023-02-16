import json
import random

#Enum de Dificuldade
from enum import Enum
class Dificuldade(Enum):
    FACIL = 1
    MEDIA = 2
    DIFICIL = 3
    ALEATORIO = 4


class Pergunta:
    def __init__(self, pergunta) -> None:
        self.codigo = pergunta['codigo']
        self.dificuldade = pergunta['dificuldade']
        self.descricao = pergunta['descricao']
        self.alternativas = pergunta['alternativas']
    
    def exibirPergunta(self):
        print("="*20 + " PERGUNTA " +"="*20)
        print(f'{self.descricao.upper()}')
        pass

    def validarResposta(self, respostaDoUsuario, respostaCorreta):
        if (respostaDoUsuario.lower() == respostaCorreta.lower()):
            print(f'PARABENS, VOCE ACERTOU :) ')
            print('\n')
            return 'true'
        else:
            print(f'QUE PENA, VOCE ERROU :( ')
            print('\n')
            return 'false'

            
    
    
class Alternativa: 
    def __init__(self, alternativa, descricao, resposta_correta) -> None:
        self.alternativa = alternativa
        self.descricao = descricao
        self.resposta_correta = resposta_correta

    def exibirAlternativa(self):
        print(f'{self.alternativa}) {self.descricao}')


#Factory para criar as instancias das perguntas, baseado no tipo de quiz fornececido pelo strategy
class PerguntaFactory:
    @staticmethod
    def criarPergunta(dificuldade: Dificuldade, pergunta):
        if dificuldade == Dificuldade.FACIL:
            return Pergunta(pergunta)
        elif dificuldade == Dificuldade.MEDIA:
            return Pergunta(pergunta)
        elif dificuldade == Dificuldade.DIFICIL:
            return Pergunta(pergunta)
        elif dificuldade == Dificuldade.ALEATORIO:
            return Pergunta(pergunta)


#Strategy para decidir qual o tipo de quiz será gerado baseado na dificuldade.
class StrategyQuiz:
    respostasValidadas = []
     
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
        
        self.exibirResultadosDoQuiz()         
        
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
        
        self.exibirResultadosDoQuiz()
    
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
        
        self.exibirResultadosDoQuiz()
    
    #Strategy aleatorio
    def __definirQuizAleatorio(self):
        print("="*50)
        print(" "*10 + " QUIZ ALEATORIO selecionado! " + " "*10)
        print("="*50)
        
        random.shuffle(self.perguntas)

        indicesAleatorios = []

        for i in range(5):
            randomIndice = random.randint(0, 16) # de (0 a 8), é porque meu json possui ao todo, nove perguntas.
            indicesAleatorios.append(randomIndice)

        for x in range(0, 5):
            self.__exibirPerguntaAoUsuario(Dificuldade.ALEATORIO, self.perguntas[indicesAleatorios[x]])
        
        self.exibirResultadosDoQuiz()
        
    # Criei este método apenas para evitar código repitido nos métodos acima, já que basicamente, todos irão seguir o mesmo fluxo.
    def __exibirPerguntaAoUsuario(self, dificuldade: Dificuldade, questao):
        perguntaCriada = PerguntaFactory.criarPergunta(dificuldade, questao)
        perguntaCriada.exibirPergunta()
        
        respostaCorreta = ''
        for alternativa in perguntaCriada.alternativas:
            novaAlternativa = Alternativa(alternativa['alternativa'], alternativa['descricao'], alternativa['resposta_correta'])
            if (novaAlternativa.resposta_correta): respostaCorreta = novaAlternativa.alternativa
            novaAlternativa.exibirAlternativa()
        
        usuario_resposta = input('Resposta: ')
        respostaValidada = perguntaCriada.validarResposta(usuario_resposta, respostaCorreta)
        self.respostasValidadas.append(respostaValidada)
        
    
    def exibirResultadosDoQuiz(self):
        acertos = 0
        erros = 0
        
        for respostaValidada in self.respostasValidadas:
            if(respostaValidada == 'true'): 
                acertos += 1
            else:
                erros += 1
        
        print("="*40)
        print('QUIZ FINALIZADO')
        print(f'ACERTOS -> {acertos}')
        print(f'ERROS  -> {erros}')
        print("="*40)   
        

class Quiz:
    @staticmethod
    def gerarQuiz(dificuldade: Dificuldade, perguntas):
        quiz = StrategyQuiz(dificuldade, perguntas)
        quiz.definirQuiz()      

#Singleton para fazer a leitura do arquivo json e extrair as perguntas
class SingletonPerguntasJSON:
    __instancia = None
    
    def __init__(self, caminhoDoArquivo):
        self.caminhoDoArquivo = caminhoDoArquivo

    def __new__(cls, *args, **kwargs):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        
        return cls.__instancia
    
    def carregarPerguntasDoJSON(self):
        dadosJSON = json.load(open(self.caminhoDoArquivo))
        perguntasJSON = dadosJSON['perguntas']
        
        return perguntasJSON
    
if __name__ == '__main__':

    singletonPerguntasJSON = SingletonPerguntasJSON('db.json')

    perguntas = singletonPerguntasJSON.carregarPerguntasDoJSON()

    print('\n')
    print("="*40)
    print('BEM VINDO AO QUIZ, SELECIONE A DIFICULDADE ABAIXO  ')
    print('\n')
    print('1 - FACIL')
    print('2 - MEDIO')
    print('3 - DIFICIL')
    print('4 - ALEATORIO')
    cmd_opcao = input('Dificuldade: ')
    print('\n')

    if (cmd_opcao == '1'):
        Quiz.gerarQuiz(Dificuldade.FACIL, perguntas)
    elif (cmd_opcao == '2'):
        Quiz.gerarQuiz(Dificuldade.MEDIA, perguntas)
    elif (cmd_opcao == '3'):
        Quiz.gerarQuiz(Dificuldade.DIFICIL, perguntas)
    elif (cmd_opcao == '4'):
        Quiz.gerarQuiz(Dificuldade.ALEATORIO, perguntas)