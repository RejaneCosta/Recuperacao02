class Tarefa:

    def __init__(self):
        self.__descricao = " "
        self.__status = " "
        self.set_status_pendente()

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_status(self):
        return self.__status

    def set_status_concluida(self):
        self.__status = "Concluida"

    def set_status_pendente(self):
        self.__status = "Pendente"

    def remover_tarefa(self, tarefa):
        self.__tarefas.remove(tarefa)

    def get_tarefa(self, posicao_tarefa):
        return self.__tarefas[posicao_tarefa]

