class DeBruijnGraph:
    """
    A De Bruijn multigraph built from a collection of strings.
    User supplies strings and k-mer length k. Nodes of the De
    Bruijn graph are k-1-mers and edges join a left k-1-mer to a
    right k‐1‐mer.
    """
    @staticmethod
    def chop(st, k):
        """ Chop a string up into k mers of given length """
        for i in range(0, len(st)-(k-1)):
            yield st[i:i+k]

    class Node:
        """ Node in a De Bruijn graph, representing a k‐1 mer """
        def __init__(self, km1mer):
            self.km1mer = km1mer

        def __hash__(self):
            return hash(self.km1mer)

        def __str__(self):
            return self.km1mer

    def __init__(self, strIter, k):
        """ Build De Bruijn multigraph given strings and k‐mer length k """
        self.G = {} # multimap from nodes to neighbors
        self.nodes = {} # maps k-1‐mers to Node objects
        self.k = k
        for st in strIter:
            for kmer in self.chop(st, k):
                km1L, km1R = kmer[:-1], kmer[1:]
                nodeL, nodeR = None, None
                if km1L in self.nodes:
                    nodeL = self.nodes[km1L]
                else:
                    nodeL = self.nodes[km1L] = self.Node(km1L)
                if km1R in self.nodes:
                    nodeR = self.nodes[km1R]
                else:
                    nodeR = self.nodes[km1R] = self.Node(km1R)
                self.G.setdefault(nodeL, []).append(nodeR)
    def show_graph(self):
        """
        A method to print the graph contents in no walk order
        :return:
        """
        for k,v in self.G.items():
            print(k, *v, sep = ", ")

if __name__ == '__main__':
    G = DeBruijnGraph(['actgctgatcgatcagcatgact'], 5)
    G.show_graph()
