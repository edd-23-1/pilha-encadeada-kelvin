# -*- coding:UTF-8 -*-
from no import No

class Pilha:
    def __init__(self, capacidade=5):
        self.__topo = None
        self.__capacidade = capacidade
        self.__qtdItens = 0


    def is_empty(self) -> bool:
        # implementação do método
        if self.__topo is None:
            return True
        
        else:
            return len(self.__topo) == 0


    def push(self, valor) -> bool:
        # implementação do método
        if (self.__qtdItens) == (self.__capacidade):
            return False
        
        else:
            novoNo = No(valor)
            novoNo.prox = (self.__topo)
            self.__topo = novoNo
            self.__qtdItens += 1
            return True


    def pop(self) -> No:
        # implementação do método
        if self.is_empty():
            return None
        
        else:
            noRemovido = self.__topo
            self.__topo = self.__topo.prox
            noRemovido.prox = None
            self.__qtdItens -= 1
            return noRemovido


    def peek(self) -> No:
        # implementação do método
        if self.is_empty():
            return None
        
        else:
            return self.__topo


    def list_items(self) -> list[str]:
        # implementação do método
        pass

    
    def get_size(self) -> int:
        # implementação do método
        pass
