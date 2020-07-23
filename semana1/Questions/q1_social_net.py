"""
Social network connectivity. 
Given a social network containing n members and a log file containing mm timestamps at which times pairs of members formed friendships, 
    design an algorithm to determine the earliest time at which all members are connected 
    (i.e., every member is a friend of a friend of a friend ... of a friend). 
    Assume that the log file is sorted by timestamp and that friendship is an equivalence relation. 
    The running time of your algorithm should be m.log(n)  or better and use extra space proportional to nn.
"""


class Connectivity():

    def __init__(self, number_members, logs):
        self.connected_components_ids = list(range(0, number_members))
        self.trees_sizes = [1] * number_members
        self.logs = logs

        # O total de subgroupos que existem na estrutura.
        self.number_of_groups = number_members

    def connected(self, component_a, component_b):

        root_a = self.root(component_a)
        root_b = self.root(component_b)

        if root_a == root_b:
            return True
        else:
            return False

    def root(self, component):

        x = component

        while x != self.connected_components_ids[x]:

            self.connected_components_ids[x] = self.connected_components_ids[
                self.connected_components_ids[x]
            ]

            x = self.connected_components_ids[x]

        return x

    def union(self, component_a, component_b):

        root_a = self.root(component_a)
        root_b = self.root(component_b)

        if root_a == root_b:
            return True

        if self.trees_sizes[root_a] < self.trees_sizes[root_b]:

            self.connected_components_ids[root_a] = self.connected_components_ids[root_b]
            self.trees_sizes[root_b] += self.trees_sizes[root_a]

        else:
            # se a arvore B for menor que a arvore A
            self.connected_components_ids[root_b] = self.connected_components_ids[root_a]
            self.trees_sizes[root_a] += self.trees_sizes[root_b]

    def earliest_time_all_connected(self):
        # Quando uma questão diz que há `m` numero de coisas
        #   (Como m numero de logs)
        #   Muito provavelmente quer dizer que é uma lista de coisas. Isso influencia
        #   na maneira de pensar na resolução.

        # Esse detalhe fez surgir a possibilidade de usar um for-loop
        #  para vasculhar os logs.
        #
        # Veja que existir uma lista de logs que relaciona quando duas pessoas se conectaram é literalmente
        #   dizer que houve uma `union(a,b)`. Para completar o algoritmo, foi adicionado
        #   a possibilidade de contar quantas arvores restaram na estrutura de dados.
        #   Quando houver apenas uma arvore, este é o momento em que a rede social está completamente conectada.

        for log in self.logs:

            if not self.connected(log.person_a, log.person_b):
                self.union(log.person_a, log.person_b)

                # Se houve uma união, então o numero de grupos restantes
                #   diminuiu em 1
                self.number_of_groups -= 1

            if self.number_of_groups == 1:
                return log.timestamp

        return False
