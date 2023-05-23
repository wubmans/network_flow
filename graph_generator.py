from graph import *

class GraphGenerator:

    a = 3

    @staticmethod
    def create(nodeCount):


        connections = [
            ("A", "B", 4),
            ("A", "D", 3),
            ("A", "F", 2),
            ("B", "C", 6),
            ("B", "D", 6),
            ("F", "D", 5),
            ("C", "H", 8),
            ("E", "H", 4),
            ("G", "E", 2),
            ("F", "E", 4),
            ("F", "G", 8),
            ("D", "E", 6),
            ("E", "B", 3),
            ("E", "C", 5)
        ]


        graph = Graph()

        source = graph.addNode(100, 400)
        source.isSource = True
        

        for j in range (3):
            for i in range(2):
                graph.addNode(300 + 250 * i, 250 + 150 * j)
        

        sink = graph.addNode(700, 400)
        sink.isSink = True
        # minDistance = -1

        # graph.connect(source, graph.nodes[2], 8)
        # graph.connect(graph.findNodeByLetter("A"), graph.findNodeByLetter("B"), 4)
        # graph.connect(source, graph.nodes[5], 4)
        
        # edge = graph.getEdge(source, graph.nodes[2])

        for connection in connections:
            graph.connect(graph.findNodeByLetter(connection[0]), graph.findNodeByLetter(connection[1]), connection[2])
        # edge.flow = 6
        

        return graph

        # for node in graph.nodes:
        #     distance = (node.x - x) ** 2 + (node.y - y) ** 2
        #     if minDistance == -1 or distance < minDistance:
        #         minDistance = distance

        # if (minDistance == -1 or minDistance > 8000):
        #     graph.addNode(x, y)
        #     points += 1
   
    # for source in graph.nodes:

    #     connections = 0

    #     while connections < 2:

    #         connected = False
    #         attemptedDestinations = []

    #         while connected == False:

    #             minDistance = -1
    #             closestNode = None
                
    #             for destination in graph.nodes:

    #                 if destination == source:
    #                     continue

    #                 if destination in graph.getNeighbors(source):
    #                     continue
                    

    #                 if destination in attemptedDestinations:
    #                     continue

    #                 distance = (source.x - destination.x) ** 2 + (source.y - destination.y) ** 2

    #                 if minDistance == -1 or distance <= minDistance:
    #                     closestNode = destination
    #                     minDistance = distance
                
    #             connected = graph.connect(source, closestNode, floor(random(10)))

    #             if connected == False:
    #                 attemptedDestinations.append(closestNode)

    #             if len(attemptedDestinations) > 7:
    #                 connected = True

    #         connections += 1