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
    def __init__(self, pergunta, dificuldade) -> None:
        self.codigo = pergunta['codigo']
        self.dificuldade = dificuldade
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
            print(f'A alternativa correta era: ({respostaCorreta})')
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
            return Pergunta(pergunta, Dificuldade.FACIL)
        elif dificuldade == Dificuldade.MEDIA:
            return Pergunta(pergunta, Dificuldade.MEDIA)
        elif dificuldade == Dificuldade.DIFICIL:
            return Pergunta(pergunta, Dificuldade.DIFICIL)
        elif dificuldade == Dificuldade.ALEATORIO:
            return Pergunta(pergunta, Dificuldade.ALEATORIO)


#Strategy para decidir qual o tipo de quiz será gerado baseado na dificuldade.
class StrategyQuiz:
    respostasValidadas = []
     
    def __init__(self, dificuldade: Dificuldade, perguntas) -> None:
        self.dificuldade = dificuldade
        self.perguntas = perguntas
        
    def definirQuiz(self):
        if self.dificuldade == Dificuldade.FACIL:
            self.definirQuizFacil()
        elif self.dificuldade == Dificuldade.MEDIA:
            self.definirQuizMedio()
        elif self.dificuldade == Dificuldade.DIFICIL:
            self.definirQuizDificil()
        elif self.dificuldade == Dificuldade.ALEATORIO:
            self.definirQuizAleatorio()
            
    #Strategy facil                    
    def definirQuizFacil(self):
        print("="*50)
        print(" "*10 + " QUIZ FACIL selecionado! " + " "*10)
        print("="*50)
        
        questoesFaceis = []
        
        for pergunta in self.perguntas:
            if(pergunta['dificuldade'] == 'FACIL'):
                questoesFaceis.append(pergunta)
                
        for questaoFacil in questoesFaceis:
            self.exibirPerguntaAoUsuario(Dificuldade.FACIL, questaoFacil)
        
        self.exibirResultadosDoQuiz()         
        
    #Strategy medio
    def definirQuizMedio(self):
        print("="*50)
        print(" "*10 + " QUIZ MEDIO selecionado! " + " "*10)
        print("="*50)
        
        questoesMedias = []
        
        for pergunta in self.perguntas:
            if(pergunta['dificuldade'] == 'MEDIA'):
                questoesMedias.append(pergunta)
                
        for questaoMedia in questoesMedias:
            self.exibirPerguntaAoUsuario(Dificuldade.MEDIA, questaoMedia)
        
        self.exibirResultadosDoQuiz()
    
    #Strategy dificil
    def definirQuizDificil(self):
        print("="*50)
        print(" "*10 + " QUIZ DIFICIL selecionado! " + " "*10)
        print("="*50)
        
        questoesDificies = []
        
        for pergunta in self.perguntas:
            if(pergunta['dificuldade'] == 'DIFICIL'):
                questoesDificies.append(pergunta)
                
        for questaoDificil in questoesDificies:
            self.exibirPerguntaAoUsuario(Dificuldade.DIFICIL, questaoDificil)
        
        self.exibirResultadosDoQuiz()


    #Strategy aleatorio
    def definirQuizAleatorio(self):
        print("="*50)
        print(" "*10 + " QUIZ ALEATORIO selecionado! " + " "*10)
        print("="*50)
        
        #Aqui, eu tenho todas as perguntas do json, eu aplico um 'shuffle' para reestruturar as posiçoes das perguntas
        #Para tentar deixar mais aleatório possivel
        random.shuffle(self.perguntas)

        for x in range(0, 5):
            self.exibirPerguntaAoUsuario(Dificuldade.ALEATORIO, self.perguntas[x])
        
        self.exibirResultadosDoQuiz()
        
    # Criei este método apenas para evitar código repitido nos métodos acima, já que basicamente, todos irão seguir o mesmo fluxo.
    def exibirPerguntaAoUsuario(self, dificuldade: Dificuldade, questao):
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

#Singleton para garantir que a leitura do arquivo seja feita uma única vez, mesmo que o arquivo
#sofra alteração durante a execução, a "variavel" que tem armazenado os dados do arquivo não vai ter seu estado alterado.
class SingletonPerguntasJSON:
    __instancia = None
    
    def __init__(self, caminhoDoArquivo):
        self.caminhoDoArquivo = caminhoDoArquivo
        self.dadosJSON = None
        self.perguntasJSON = []
    
    def carregarPerguntasDoJSON(self):
        if self.dadosJSON is None:
            self.dadosJSON = json.load(open(self.caminhoDoArquivo))
            self.perguntasJSON = self.dadosJSON['perguntas']
        
        return self.perguntasJSON
    
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