# 1. Propósito
---
Esta tarefa tem os seguintes propósitos:
- Desenvolver as habilidades de criação e manipulação de estruturas de dados do tipo pilha (stack);
- Implementar e validar os conceitos relacionados ao métodos de esturas de dados pilha.

# 2. Orientações
---

As subsessões a seguir orientam sobre o uso de soluções as quais poderão auxiliar na realização dessa tarefa, bem como os aspectos gerais relativos à implementação (código fonte) da sua solução.

## 2.1. Instalação do framework pytest
---
A estrutura do código fonte está montada para ser validada com a framework pytest, o qual poderá ser instalado com o comando:

```console
$ pip install pytest
```

Você não está obrigado a instalar o pytest e rodar os testes de validação antes do envio da tarefa, entretanto pode ser bastante útil para que você consiga identificar onde estão os pontos de falhas no seu projeto.

Para realizar um teste de validação da sua implementação, basta executar o seguinte comando:

```console
$ pytest test_1.py -v
```

O pytest permite que você realize o teste sobre mais de um arquivo. Portanto, também é válido o comando:

```console
$ pytest test_1.py test_2.py test_3.py test_4.py test_5.py test_6.py -v
```
No caso de todos os testes serem aprovados, o resultado de saída no terminal deverá ser algo como mostrado em: 

```console
$ pytest test_1.py test_2.py test_3.py test_4.py test_5.py test_6.py -v --no-header
==================================== test session starts =====================================
collected 12 items                                                                           

test_1.py::test_pilha_is_empty_true PASSED                                             [  8%]
test_1.py::test_pilha_is_empty_false PASSED                                            [ 16%]
test_2.py::test_push_em_pilha_cheia PASSED                                             [ 25%]
test_2.py::test_push_em_pilha_vazia PASSED                                             [ 33%]
test_3.py::test_pilha_peek_com_itens PASSED                                            [ 41%]
test_3.py::test_pilha_peek_sem_itens PASSED                                            [ 50%]
test_4.py::test_pilha_pop_sem_itens PASSED                                             [ 58%]
test_4.py::test_pilha_pop_com_itens PASSED                                             [ 66%]
test_5.py::test_pilha_list_items_com_elementos PASSED                                  [ 75%]
test_5.py::test_pilha_list_items_sem_elementos PASSED                                  [ 83%]
test_6.py::test_pilha_get_size_com_itens PASSED                                        [ 91%]
test_6.py::test_pilha_get_size_sem_itens PASSED                                        [100%]

===================================== 12 passed in 0.06s =====================================
```

No caso de todos os testes falherem, o resultado de saída no terminal poderá ser algo como mostrado em: 

```console
$ pytest test_1.py test_2.py test_3.py test_4.py test_5.py test_6.py -v --no-header
================================================= test session starts =================================================
collected 12 items                                                                                                    

test_1.py::test_pilha_is_empty_true PASSED                                                                      [  8%]
test_1.py::test_pilha_is_empty_false PASSED                                                                     [ 16%]
test_2.py::test_push_em_pilha_cheia PASSED                                                                      [ 25%]
test_2.py::test_push_em_pilha_vazia FAILED                                                                      [ 33%]
test_3.py::test_pilha_peek_com_itens PASSED                                                                     [ 41%]
test_3.py::test_pilha_peek_sem_itens PASSED                                                                     [ 50%]
test_4.py::test_pilha_pop_sem_itens PASSED                                                                      [ 58%]
test_4.py::test_pilha_pop_com_itens PASSED                                                                      [ 66%]
test_5.py::test_pilha_list_items_com_elementos PASSED                                                           [ 75%]
test_5.py::test_pilha_list_items_sem_elementos PASSED                                                           [ 83%]
test_6.py::test_pilha_get_size_com_itens PASSED                                                                 [ 91%]
test_6.py::test_pilha_get_size_sem_itens PASSED                                                                 [100%]

====================================================== FAILURES =======================================================
______________________________________________ test_push_em_pilha_vazia _______________________________________________

    def test_push_em_pilha_vazia():
    
        try:
            exists = os.path.exists("pilha.py")
            assert exists == True
        except:
            sys.exit()
    
        pilha = Pilha()
    
>       assert pilha.push(2) == True
E       assert False == True
E        +  where False = <bound method Pilha.push of <pilha.Pilha object at 0x1075b2f20>>(2)
E        +    where <bound method Pilha.push of <pilha.Pilha object at 0x1075b2f20>> = <pilha.Pilha object at 0x1075b2f20>.push

test_2.py:36: AssertionError
=============================================== short test summary info ===============================================
FAILED test_2.py::test_push_em_pilha_vazia - assert False == True
============================================ 1 failed, 11 passed in 0.07s =============================================
```

Para mais detalhes e informações sobre o framework consultar no [link](https://docs.pytest.org/en/7.3.x/contents.html).

## 2.2. Implementação da solução
---

Você deverá implementar os **métodos da classe Pilha** no arquivo **pilha.py**, os quais ainda não foram implementados. Esteja atento ao tipo de retorno de cada método, pois isso irá impactar diretamente na avaliação da sua solução após você enviar o commit com as suas implementações para o repositório remoto.

Após concluir a tarefa, você deverá realizar um **git push** para entregar a sua atividade. Você poderá realizar tantos envios ao repositório remoto quanto desejar. Entretanto, esteja atento ao prazo de entreda da atividade para não realizar a entrega com atraso, pois isso irá impactar sobre a nota da atividade. 

Os testes de validação da pontuação realizados pelo GitHub-Classroom não ocorrem imediatamente após o envio do push para o servidor. Normalmente, o GitHub levará o tempo de alguns segundos para realizar o teste sobre a solução enviada por você. Você deverá atualizar a página no GitHub-Classroom a cada 10s, caso não perceba a mudança no resultado da pontuação, até que o GitHub faça o computo dos seus pontos a partir da execução dos testes sobre a sua entrega.

Esteja atento aos tipos de retorno de cada método, os quais se encontram descritos com _type hint_ no próprio método.

## 2.3. Prazo de entrega
---

O prazo de entrega encontra-se descrito no ambiente do Google Sala de Aula da turma e também do GitHub Classroom.


# 3. Tarefas
---

Segue a relação de tarefas a serem observadas na implementação de cada método e a respectiva pontuação do método destacada em parênteses. Toda a tarefa valerá **20pts**, o que corresponde a **20%** da nota da primeira etapa.

- [x] Estudar e analizar os conceitos e técnicas para implementação da estrutura de dados do tipo pilha
- [ ] **(3pts)** Implementar o método **is_empty()**
  - [ ] Deve retornar um boolean True se não houver itens (Nó) na pilha ou False, caso contrário
- [ ] **(5pts)** Implementar o método **push()**, o qual deve receber como entrada um valor para criar um nó que deverá ser inserido na pilha
  - [ ] Criar um objeto Nó a partir do valor recebido pelo método
  - [ ] Deve retornar um boolean True se conseguir inserir um item (Nó) na pilha
  - [ ] Caso a pilha tenha alcançado a sua capacidade máxima, o item (Nó) não deve ser inserido na pilha e método deverá retornar um boolean False
- [ ] **(5pts)** Implementar o método **pop()**, o qual deve retornar o último item (Nó) inserido na pilha e remover esse item da pilha
  - [ ] Caso a pilha esteja vazia deverá retornar um None
  - [ ] Caso a pilha possua um ou mais itens, o último item (Nó) inserido na pilha deve ser removido da e retornado pelo método
- [ ] **(2pts)** Implementar o método **peek()**, o qual deve retornar o último item (Nó) inserido na pilha SEM remover esse item da pilha
  - [ ] Caso a pilha esteja vazia deverá retornar um None
  - [ ] Caso a pilha possua um ou mais itens, o último item (Nó) inserido na pilha deve ser retornado pelo método
- [ ] **(3pts)** Implementar o método **list_items()**, o qual deve retornar uma lista de strings dos itens (Nó) inseridos na pilha
  - [ ] Caso a pilha esteja vazia deverá retornar uma lista contendo apenas strings ['Topo da Pilha:\n', 'Base da Pilha\n']
  - [ ] Caso a pilha possua um ou mais itens, o primeiro elemento da lista deve ser a string 'Topo da Pilha:\n', seguida das strings dos valores que compõem a pilha (do topo para a base), e o último elemento da lista deve ser a string 'Base da Pilha\n'
- [ ] **(2pts)** Implementar o método **get_size()**, o qual deve retornar um int
  - [ ] O método deverá retornar ZERO, caso a pilha esteja vazia, ou, caso possua algum item na pilha, o valor relativo à quantidade de itens presentes na pilha