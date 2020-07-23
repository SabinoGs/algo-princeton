class WeightedQuickUnion():

    def __init__(self, n_elements):
        self.connected_components_ids = list(range(0, n_elements))
        self.tree_sizes = [1] * n_elements

    def root(self, element_a):
        x = element_a

        while x != self.connected_components_ids[x]:
            # Da dois passos em direção a raiz. Efetivamente seta um nó para
            #   ter a raiz no seu "avô". Ajuda a achatar a arvore.

            self.connected_components_ids[x] = self.connected_components_ids[
                self.connected_components_ids[x]
            ]
            x = self.connected_components_ids[x]

        return x

    def union(self, element_a, element_b):

        root_a = self.root(element_a)
        root_b = self.root(element_b)

        if root_a == root_b:
            return None  # faz nada. já são unidos

        if self.tree_sizes[root_a] < self.tree_sizes[root_b]:
            # Une a arvore A em B.
            self.connected_components_ids[root_a] = root_b

            # Adiciona o numero de elementos de A em B
            self.tree_sizes[root_b] += self.tree_sizes[root_a]
        else:
            # Une a Arvore B em A
            self.connected_components_ids[root_b] = root_a

            # Adiciona o numero de elementos de B em A
            self.tree_sizes[root_a] += self.tree_sizes[root_b]

    def connected(self, element_a, element_b):

        root_a = self.root(element_a)
        root_b = self.root(element_b)

        if root_a == root_b:
            return True
        else:
            return False
