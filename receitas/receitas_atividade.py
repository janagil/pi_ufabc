def add_despensa():
    # criar um dicionario onde o usuário que insere os valores
    despensa = {}

    num_max = int(input('Quantos itens deseja adicionar na sua despensa? '))

    while len(despensa) < num_max:
        nome_despensa = input('Insira o nome do item: ')
        quant_item = int(input('Insira a quantidade do item: '))
        despensa[nome_despensa] = quant_item
    return despensa  # {'leite': 3, 'ovos': 1, 'manteiga': 1}


def vezes_receita(receita, despensa):
    # função criada em aula pra calcular quantas vezes o usuario pode fazer tal receita
    nomes_ingredientes = list(receita)
    ingrediente1 = nomes_ingredientes[0]
    ingrediente2 = nomes_ingredientes[1]
    ingrediente3 = nomes_ingredientes[2]
    n_ingrediente1 = despensa[ingrediente1] // receita[ingrediente1]
    n_ingrediente2 = despensa[ingrediente2] // receita[ingrediente2]
    n_ingrediente3 = despensa[ingrediente3] // receita[ingrediente3]
    return min(n_ingrediente1, n_ingrediente2, n_ingrediente3)

def subtrair_receita(receita, despensa):
    # função para calcular se é possível fazer 1 vez cada receita
    nova_despensa = despensa.copy()
    for ingrediente in receita:
        if ingrediente in nova_despensa:
            nova_despensa[ingrediente] -= receita[ingrediente]
    return nova_despensa

def calcular_todas_receitas(receitas, despensa):
    possibilidades = []
    for receita in receitas:
        despensa_atualizada = subtrair_receita(receita, despensa)
        vezes = vezes_receita(receita, despensa_atualizada)
        possibilidades.append(vezes)
    return min(possibilidades)

def main():
    # receitas disponíveis (pao, bolo, pudim, macarrao)
    pao = {'farinha': 50, 'fermento': 5, 'oleo': 10}
    bolo = {'farinha': 100, 'acucar': 50, 'fermento': 10}
    pudim = {'leite': 5, 'ovos': 4, 'acucar': 50}
    macarrao = {'tomate': 2, 'massa': 1, 'sal': 20}

    print('''Receitas
Para começar, adicione itens na sua dispensa para poder checar quantas vezes é possível fazer a receita escolhida.
Caso queria calcular se é possível fazer todas as receitas 1 vez, insira todos os 9 ingredientes na despensa 
(caso não queira o ingrediente, colocar quantidade 0)''')
    
    despensa = add_despensa()

    escolha = input('\nQual receita deseja fazer?\nOpções:\n- Pão\n- Bolo\n- Pudim\n- Macarrão\n')
    
    if escolha == 'pao':
        print(f'É possível fazer {vezes_receita(pao, despensa)} pães.')
    elif escolha == 'bolo':
        print(f'É possível fazer {vezes_receita(bolo, despensa)} bolos.')
    elif escolha == 'pudim':
        print(f'É possível fazer {vezes_receita(pudim, despensa)} pudins.')
    elif escolha == 'macarrao':
        print(f'É possível fazer {vezes_receita(macarrao, despensa)} porções de macarrão.')

    opcao = input('\nDeseja calcular se é possível fazer todas as receitas? (s/n) ')
    if opcao.lower() == 's':
        receitas = [pao, bolo, pudim, macarrao]
        vezes_todas_receitas = calcular_todas_receitas(receitas, despensa)
        print(f'É possível fazer todas as receitas pelo menos {vezes_todas_receitas} vez(es).')

main()