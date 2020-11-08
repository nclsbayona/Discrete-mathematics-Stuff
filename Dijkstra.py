import matplotlib.pyplot as plt
from networkx import Graph as nxGraph
from networkx import dijkstra_path, draw


class Node:
    __slots__=["name","edges"]

    def __init__(self, name) -> None:
        self.name=name
        self.edges=list()

    def __eq__(self, name):
        return self.name==name

    def __ne__(self, name):
        return self.name!=name
    
    def addEdge(self, end, directed=False, weight=0):
        edge=Edge(self, end, directed=directed, weight=weight)
        if edge not in self.edges:
            self.edges.append(edge)
            return True
        return False
    
    def edgeLookup(self, end):
        for edge in (self.edges):
            if edge.end==end:
                return edge
        return False

    def returnEdgesAsTuple(self):
        edges=list()
        for edge in (self.edges):
            edges.append(edge.edgeAsTuple())
        return edges

    def __str__(self) -> str:
        a=f"Name: {self.name}\n\t"
        for edge in (self.edges):
            a+=f"{edge}\n\t"
        a+='\n'
        return a


class Edge:
    __slots__=["start", "end", "directed","weight"]

    def __init__(self, start: Node, end: Node, directed=False, weight=0) -> None:
        self.start=start.name
        self.end=end.name
        self.directed=directed
        self.weight=weight
    
    def edgeAsTuple(self):
        tp=(self.start, self.end, self.weight)
        return tp

    def __eq__(self, edge):
        return self.start==edge.start and self.end==edge.end and self.directed==edge.directed and self.weight==edge.weight

    def __ne__(self, edge):
        return self.start!=edge.start or self.end!=edge.end or self.directed!=edge.directed or self.weight!=edge.weight

    def __str__(self):
        return f"Start: {self.start}, end: {self.end}, directed: {str(self.directed)} and weight {str(self.weight)}"


class Graph:

    __slots__=["numberOfNodes","nodes"]
    def __init__(self):
        self.numberOfNodes=0
        self.nodes=list()

    def dijkstra(self, start, end):
        graph=nxGraph()
        edges=list()
        for node in (self.nodes):
            edges.extend(node.returnEdgesAsTuple())
        graph.add_weighted_edges_from(edges)
        return dijkstra_path(graph, start, end)
        

    def searchNode(self, name)->Node:
        try:
            for node in self.nodes:
                if node==name:
                    return node
            raise Exception
        except:
            return False

    def addNode(self, name):
        if self.searchNode(name=name)==False:
            self.nodes.append(Node(name))
            self.numberOfNodes+=1
            return True
        return False

    def addEdge(self, start, end, directed=False, weight=None):
        self.addNode(start)
        self.addNode(end)
        startN=self.searchNode(start)
        endN=self.searchNode(end)
        try:
            
            startN.addEdge(endN, directed=directed, weight=weight)
            if bool(directed)==False:
                endN.addEdge(startN, directed, weight)

        except:
            return False

        return True

    def printG(self):
        for node in self.nodes:
            print (node)

    def __str__(self):
        graph=nxGraph()
        edges=list()
        for node in (self.nodes):
            edges.extend(node.returnEdgesAsTuple())
        graph.add_weighted_edges_from(edges)
        draw(graph, with_labels=True)
        plt.show()

def graphMenu():
    return "1. Add Node\n2. Add edge\n3. Dijkstra Algorithm\n4. Print Graph Textual\n5. Print Graph Visually"

if __name__=="__main__":
    g=Graph()
    node1=None
    node2=None
    edge=None
    weight=None
    dijkstraWeight=None
    directed=None
    choice=None
    while (choice!=-1):
        dijkstraWeight=0
        print('\n\n'+graphMenu()+'\n')
        choice=int(input("Choice: "))
        if choice==1:
            node1=input("Node name: ")
            g.addNode(node1)
        elif choice==2:
            node1=input("Start node name: ")
            node2=input("End node name: ")
            weight=int(input("Edge weight: "))
            directed=input("Directed(1/0): ")
            if directed!="0":
                g.addEdge(node1, node2, directed=True, weight=weight)
            else:
                g.addEdge(node1, node2, weight=weight)
        elif choice==3:
            try:
                node1=input("Start node name: ")
                node2=input("End node name: ")
                dp=g.dijkstra(node1, node2)
                for i in range (len(dp)-1):
                    edge=(g.searchNode(dp[i]).edgeLookup(dp[i+1]))
                    if (edge.start!=str(dp[i]) or edge.end!=str(dp[i+1])):
                        print (dp[i].name, dp[i+1].name, dp, "Not working")
                        raise Exception
                    else:
                        dijkstraWeight+=edge.weight
                print (f"Shortest path: {dp}, weight: {dijkstraWeight}")
            except:
                print ("Impossible")
        elif choice==4:
            g.printG()
        elif choice==5:
            try:
                print (g)
            except:
                pass
