class Tarefas:
    def __init__(self,d, i, f):
        self.descricao = d
        self.inicio = i
        self.fim = f
        self.tam= f - i


t1 = Tarefas("t1", 1,2)
t2 = Tarefas("t2", 1,3)
t3 = Tarefas("t3", 3,5)
t4 = Tarefas("t4", 8,9)

lista = [t4, t2, t3, t1]


lista.sort(key=lambda x: x.tam)
for item in lista:
    print(item.tam)
solucao = []
solucao.append(lista[0])
pos = 0
for i in range(1, len(lista), +1):
    if lista[i].inicio >= lista[pos].fim:
        solucao.append(lista[i])
        pos = 1
print(len(solucao))
    