# NÃO ALTERE O CÓDIO DESSE ARQUIVO

# Tests for Stack Task
# Simple Array Stack

import os.path
import sys
from pilha import Pilha


def test_pilha_list_items_com_elementos():
    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            pilha.push(item[:-1])

    result = pilha.list_items()
    expected = [
        "Topo da Pilha:\n",
        "5\n",
        "4\n",
        "3\n",
        "2\n",
        "1\n",
        "Base da Pilha\n",
    ]

    assert result == expected


def test_pilha_list_items_sem_elementos():
    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha()

    result = pilha.list_items()
    expected = [
        "Topo da Pilha:\n",
        "Base da Pilha\n",
    ]
    
    assert result == expected
