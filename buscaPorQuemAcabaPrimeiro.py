class Tarefas:
    def __init__(self,d, i, f):
        self.descricao = d
        self.inicio = i
        self.fim = f


t1 = Tarefas("t1", 1,2)
t2 = Tarefas("t2", 1,2)
t3 = Tarefas("t3", 1,2)
t4 = Tarefas("t4", 1,2)

lista = [t4, t2, t3, t1]


lista.sort(key=lambda x: x.fim)
for item in lista:
    print(item.fim)
solucao = []
solucao.append(lista[0])
pos = 0
for i in range(1, len(lista), +1):
    if lista[i].inicio >= lista[pos].fim:
        solucao.append(lista[i])
        pos = 1
print(len(solucao))