# NÃO ALTERE O CÓDIO DESSE ARQUIVO

# Tests for Stack Task
# Simple Array Stack

import os.path
import sys
from pilha import Pilha
from no import No


def test_pilha_pop_sem_itens():
    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha()

    assert pilha.pop() == None


def test_pilha_pop_com_itens():
    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            pilha.push(item[:-1])

    expected = No('5')
    result = pilha.pop()

    assert expected.dado == result.dado and pilha.peek().dado == '4'
