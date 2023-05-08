# NÃO ALTERE O CÓDIO DESSE ARQUIVO

# Tests for Stack Task
# Simple Array Stack

import os.path
import sys
from pilha import Pilha


def test_pilha_is_empty_true():

    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha()

    assert pilha.is_empty() == True


def test_pilha_is_empty_false():

    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha()
    pilha.push(1)

    assert pilha.is_empty() == False
