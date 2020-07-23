class UnionFind():

    def __init__(self, n_elementos):
        self.connected_components_ids = list(range(n_elementos))
        self.tamanho_lista = n_elementos

    def union(self, elemento_a, elemento_b):
        id_elemento_a = self.connected_components_ids[elemento_a]
        id_elemento_b = self.connected_components_ids[elemento_b]

        for i in range(0, self.tamanho_lista):
            if self.connected_components_ids[i] == id_elemento_a:
                self.connected_components_ids[i] = id_elemento_b

    def connected(self, elemento_a, elemento_b):
        connected = False
        id_a = self.connected_components_ids[elemento_a]
        id_b = self.connected_components_ids[elemento_b]

        if id_a == id_b:
            connected = True

        return connected
