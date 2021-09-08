from agenda import Agenda
from contato import Contato
from tarefa import Tarefa


class Main:

    def __init__(self):
        self.agenda = Agenda()
        self.em_execucao = True
        self.agenda.set_proprietario("Rejane")
        self.agenda.set_ano("2021")

    def mostar_menu(self):
        print("======================")
        print(" AGENDA VIRUTAL ")
        print("======================")
        print("selecione uma opção: ")
        print("-----------------------")
        print("1 - Cadastrar Contato")
        print("2 - Listar contato")
        print("3 - Excluir contato")
        print("4 - Criar tarefa")
        print("5 - Listar tarefas")
        print("6 - Excluir tarefas")
        print("7 - Sair")
        print("======================")

    def ler_opcao_menu(self):
        opcao = input(" > ")


        if (opcao == "1"):
            self.cadastrar_contato()
        elif (opcao == "2"):
            self.listar_contatos()
        elif (opcao == "3"):
            self.excluir_contato()
        elif (opcao == "4"):
            self.criar_tarefa()
        elif (opcao == "5"):
            self.listar_tarefas()
        elif (opcao == "6"):
            self.excluir_tarefas()
        elif (opcao == "7"):
            print("Finalizando processo, após muito estudo")
            self.em_execucao = False
            return


    def cadastrar_contato(self):
        print(">>Cadastro de Contato<<")
        nome = input("Nome do contato: ")
        telefone = input("Telefone do contato: ")
        email = input("Informe e-mail do contato: ")

        contato = Contato()
        contato.set_nome(nome)
        contato.set_telefone(telefone)
        contato.get_email(email)

        self.agenda.add_contato(contato)
        print("Contato adicionado a lista")

    def listar_contatos(self):
        print("Contatos Cadastrados")
        contatos_da_agenda = self.agenda.get_contatos()
        for indice, contato in enumerate(contatos_da_agenda):
            print("Contato nº " + str(indice) + ". Contato: " + contato.get_nome() + " | Tel: " + contato.get_telefone())

    def excluir_contato(self):
        self.excluir_contato()
        indice_para_excluir = input("Digite o número do contato que deseja excluir: ")

        try:
            contato_selecionado = self.agenda.get_contato(int(indice_para_excluir))
        except:
            print("Contato Inválido")
            return

        self.agenda.remover_contato(contato_selecionado)
        print("Contato Excluido")

    def cadastrar_tarefa(self):
        print("Nova Tarefa")
        descricao = input("Descrição: ")
        status = input("Concluida: 1 - Sim | 2 - Não")

        tarefa = Tarefa()
        tarefa.set_descricao(descricao)
        if (status == "1"):
            tarefa.set_status_concluida()
        elif (status == "2"):
            tarefa.set_status_pendente()
        else:
            print("Status Inválido")

            self.agenda.add_tarefas(tarefa)
            print("Tarefa adicionado")

    def listar_tarefas(self):
        print("Tarefas Cadastradas")
        tarefas_da_agenda = self.agenda.get_tarefas()
        for indice, tarefa in enumerate(tarefas_da_agenda):
            print("Tarefa nº " + str(indice) + " - " + tarefa.get_descricao() + " | Status: " + tarefa.get_status())

    def excluir_tarefa(self):
        self.listar_tarefas()
        indice_para_excluir = input("Digite o número da tarefa que deseja excluir: ")

        try:
            tarefa_selecionada = self.agenda.get_tarefa(int(indice_para_excluir))
        except:
            print("Tarefa Inválido")
            return

        self.agenda.remover_tarefa(tarefa_selecionada)
        print("Tarefa Excluida")




