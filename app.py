import os
destinos = [{"nome": "Pedro Pedro", "Destino": "Morumbi", "ativo": True},
           {"nome": "Isabel Roberta", "Destino": "Jardir São Paulo", "ativo": False},
           {"nome": "Vinicius Rosa", "Destino": "jardir Europa", "ativo": True},
           {"nome": "Gustavo Erique", "Destino": "Centro", "ativo": True}]
    
def exibir_titulo():
    print("""táxi\n""")


def exibir_opcao():
    print('1. Cadastrar Viajante')
    print('2. Listar Viagem')
    print('3. Ativar Cadrastro')
    print('4. Sair\n')

def escolher_opcao():

    def exibir_subtitulo(texto):
        os.system('clear')
        print(texto)
        print(" ")

    def retorna_menu():
        input("Aperte para retornar")
        main()


    def cadrastro_viagem():
        exibir_subtitulo("Cadastro de viagens")
        destino_viagem = input("Digite o destino da sua viagem: ")
        dados_da_viagem = {"nome": nome_pessoa, "destino": destino_viagem,"ativo": True }
        destinos.append(destino_viagem)
        print(f" A viagem {destino_viagem} foi cadrastada com exito")
        retorna_menu()

    def lista_viagens():
        exibir_subtitulo("Lista de Viagens")
        for destino in destinos:
            nome_pessoa = destino["nome"]
            destino_pessoa = destino["Destino"]
            ativo = destino["ativo"]
            print(f" - {nome_pessoa} | {destino_pessoa} | {ativo} ")
        retorna_menu()

    def ativar_cadrastro():
        exibir_subtitulo("Ativar cadastro de viagem")
        nome_pessoa = input("digite o endereço:")
        nome_encontro = False
        for destino in destinos:
            if nome_pessoa == destino["nome"]
            nome_encontro = True
            destino["ativa"] = not destino
            mensagem = f"{nome_pessoa} teve sua viagem ativada"

        retorna_menu()
        

    def finalizar_app():
        os.system('clear')
        print("Finalizando programa")

    def opcao_invalida():
        print("Opçao Invalida")
        input("Aperte um botão para retornar")
        main()

    opcao_escolhida = int(input('Escolha uma opção:'))
    try:
        if opcao_escolhida == 1:
            cadrastro_viagem()
        elif opcao_escolhida == 2:
            lista_viagens()
        elif opcao_escolhida == 3:
            ativar_cadrastro()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_titulo()
    exibir_opcao()
    escolher_opcao()

if __name__ == "__main__":
    main()

