class UnionFindCanonical():

    def __init__(self, number_of_elements):
        """Pra dar conta de resolver essa questão é necessário, de alguma maneira, manter a contagem dos elementos dos componentes.

        Se tentarmos selecionar os elementos de um Connected Component (CC) e varrer eles, será uma busca, no mínimo, linear.

        Agora, se atualizarmos a lista de contagem, toda vez que realizarmos uma union(a,b), 
            vamos economizar um pouco de tempo mantendo contagem da lista. 

        Mas como?

        inicializamos uma lista nova de contagem, ex:

        large = 0,1,2,3,4,5,6,7,8,9 <- Pois há 10 componentes conectados. 
        Quando realizarmos um union(a,b) verificamos se large[a] > large[b], se sim large[root(b)] == large[a]. E vice-versa.

        Mas porque adicionamos o root(a) no indice do large? 
         R: Pq assim não temos que atualizar a lista large inteira. 
            Atualiza somente em 1 lugar toda vez que realizamos a union. 
            Assim o método find(a) deverá buscar qual é o número da lista `large` no índice root(a): large[root(a)]

            (opinião): 
                Acabamos com a lista large desatualizada nos indices não root. 
                Mas o root sempre vai ter o elemento canônico que é esperado
        """

        self.connected_components_id = list(range(number_of_elements))
        self.large = list(range(number_of_elements))

        self.trees_sizes = [1] * number_of_elements

    def root(self, component_a):

        x = component_a

        while x != self.connected_components_id[x]:
            self.connected_components_id[x] = self.connected_components_id[
                self.connected_components_id[x]
            ]
            x = self.connected_components_id[x]

        return x

    def connected(self, component_a, component_b):
        return self.root(component_a) == self.root(component_b)

    def find(self, component):
        return self.large[self.root(component)]

    def union(self, component_a, component_b):

        print(" -> unindo ", component_a, component_b)

        root_a = self.root(component_a)
        root_b = self.root(component_b)

        large_a = self.large[root_a]
        large_b = self.large[root_b]

        if self.trees_sizes[root_a] < self.trees_sizes[root_b]:
            self.connected_components_id[root_a] = self.connected_components_id[root_b]
            self.trees_sizes[root_b] += self.trees_sizes[root_a]

        else:
            self.connected_components_id[root_b] = self.connected_components_id[root_a]
            self.trees_sizes[root_a] += self.trees_sizes[root_b]

        # Porque isso acontece?
        if large_a > large_b:
            self.large[root_b] = large_a
        else:
            self.large[root_a] = large_b

        print(" -> Componentes: ", self.connected_components_id,
              "Large: ", self.large)


if __name__ == "__main__":
    uf = UnionFindCanonical(10)
    uf.union(0, 2)
    uf.union(8, 4)
    print(uf.find(0) == 2)
    print(uf.find(4) == 8)
    uf.union(0, 4)
    print(uf.find(0) == 8)
    print(uf.find(2) == 8)
    uf.union(0, 6)
    print(uf.find(6) == 8)
    uf.union(1, 9)
    uf.union(1, 2)
    print(uf.find(4) == 9)
    print(uf.large)
