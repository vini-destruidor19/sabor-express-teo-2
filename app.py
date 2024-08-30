import os
viagens = [{"nome": "gabriel", "destino": "Morumbi 1", "ativo": True},
           {"nome": "Vini", "destino": " Jardir são paulo", "ativo": True},
           {"nome": "samuel", "destino": "Portal", "ativo": True}]
    
def exibir_titulo():
    print("""taxi\n""")


def exibir_opcao():
    print('1. Cadastrar Viajante')
    print('2. Listar Viagem')
    print('3. Ativar Cadrastro')
    print('4. Sair\n')

def escolher_opcao():

    def exibir_subtitulo(texto):
        os.system('cls')
        linha = "-" *len(texto)
        print(linha)
        print(texto)
        print(" ")

    def retorna_menu():
        input("Aperte para retornar")
        main()


    def cadrastro_viagem():
        exibir_subtitulo("Cadastro de viagens")
        nome_pessoa = input("Digite seu nome: ")
        destino_pessoa = input(f"Insira seu destino: ")
        dados_da_pessoa = {"nome":nome_pessoa, "destino":destino_pessoa, "ativo":True}
        viagens.append(dados_da_pessoa)
        print(f" A viagem {nome_pessoa} foi cadrastada com exito")
        retorna_menu()

    def lista_viagens():
        exibir_subtitulo("Lista de Viagens")
        for viagem in viagens:
            nome_pessoa = viagem["nome"]
            destino_pessoa = viagem["destino"]
            ativo = "ativo" if viagem["ativo"] else "desativado"
            print(f" - {nome_pessoa.ljust(20)} | {destino_pessoa} | {ativo} ")
        retorna_menu()

    def ativar_cadrastro():
        exibir_subtitulo("Ativar cadastro de viagem")
        nome_pessoa = input("Digite o nome para ativar a viagem: ")
        nome_encontro = False
        for viagem in viagens:
            if nome_pessoa == viagem["nome"]:
                nome_encontro = True
                viagem["ativo"] = not viagem["ativo"]
                mensagem = f"{nome_pessoa} teve sua viagem ativada" if viagem["ativo"] else f"O cadrastro de {nome_pessoa} teve a viagem desativada"
                print(mensagem)
        if not nome_encontro:
            print("Nao encontrado, favor digite para voltar")
        retorna_menu()
        

    def finalizar_app():
        os.system('cls')
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
    os.system('cls')
    exibir_titulo()
    exibir_opcao()
    escolher_opcao()

if __name__ == "__main__":
    main()

