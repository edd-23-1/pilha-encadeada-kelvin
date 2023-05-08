# NÃO ALTERE O CÓDIO DESSE ARQUIVO

# Tests for Stack Task
# Simple Array Stack

import os.path
import sys
from pilha import Pilha


def test_push_em_pilha_cheia():

    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha(1)

    pilha.push(1)

    assert pilha.push(2) == False


def test_push_em_pilha_vazia():

    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha()

    assert pilha.push(2) == True
