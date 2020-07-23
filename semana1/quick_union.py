class QuickUnion():

    def __init__(self, n_elementos):
        self.connected_components_ids = list(range(n_elementos))

    def root_of_element(self, element):
        x = element

        while x != self.connected_components_ids[x]:
            x = self.connected_components_ids[x]

        return x

    def connected(self, element_a, element_b):

        root_a = self.root_of_element(element_a)
        root_b = self.root_of_element(element_b)

        if root_a == root_b:
            return True
        else:
            return False

    def union(self, element_a, element_b):

        root_a = self.root_of_element(element_a)
        root_b = self.root_of_element(element_b)

        self.connected_components_ids[root_a] = root_b
