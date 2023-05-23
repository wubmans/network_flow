def drawArrow(source, target, thickness, shrink = 0.85):
     
    strokeWeight(thickness / 2)
    strokeCap(ROUND)
    
    
    a = thickness #dist(x1, y1, x2, y2) / 50

    dx = target.x - source.x
    dy = target.y - source.y

    pushMatrix()
    translate(source.x + shrink * dx, source.y + shrink * dy)
    rotate(atan2(dy, dx))
    triangle(- a * 2 , - a, 0, 0, - a * 2, a)
    popMatrix()

    strokeWeight(thickness)
    line(source.x + (1 - shrink) * dx,  source.y + (1 - shrink) * dy, source.x + shrink * dx,  source.y + shrink * dy)  

class Graph:
    
    nodes = []
    edges = []

    stateCounter = 0

    augmentingPath = None

    showFlow = True
    showResidual = True
    showCapacity = True
    noMorePaths = False
    
    def __init__(self):
        pass
    
    def addNode(self, x, y):
        
        node = Node(x, y)
        self.nodes.append(node)
        node.letter = chr(len(self.nodes) + 64)
        return node
                
    def draw(self):
            
        for edge in self.edges:
            edge.draw(self.showFlow, self.showResidual, self.showCapacity)

        for node in self.nodes:
            node.draw()


        if self.augmentingPath is not None:
            for edge in self.augmentingPath:
                stroke(0, 0, 255, 60)
                fill(0, 0, 255, 60)
                line(edge.source.x, edge.source.y, edge.target.x, edge.target.y)

        if (self.noMorePaths):
            fill(128, 0, 0)
            textAlign(LEFT)
            text("No more augmenting paths", 10, 20)

    def findNodeByLetter(self, letter):
        for node in self.nodes:
            if node.letter == letter:
                return node
            
    def findSource(self):
        for node in self.nodes:
            if node.isSource:
                return node
            
    def findSink(self):
        for node in self.nodes:
            if node.isSink:
                return node

    def connect(self, source, target, capacity):
        for edge in self.edges:
            if edge.source == source and edge.target == target:
                continue
            if edge.target == source and edge.source == target:
                continue
            # if intersect(edge.source, edge.target, source, target):
            #     return False

        self.edges.append(Edge(source, target, capacity))
        return True

    def getNeighbors(self, node):
        neighbors = []

        for edge in self.edges:
            if edge.source == node and edge.capacity - edge.flow > 0:
                neighbors.append(edge.target)
            # if edge.target == node:
            #     neighbors.append(edge.source)

        return neighbors

    def getEdge(self, source, target):

        for edge in self.edges:
            if edge.source == source and edge.target == target:
                return edge
            if edge.target == source and edge.source == target:
                return edge

    def hasPathToSink(self, node, path):

        neigbors = self.getNeighbors(node)

        for neighbor in neigbors:

            if self.hasPathToSink(neighbor, path):
                path.insert(0, neighbor)
                return True
            if neighbor.isSink:
                path.insert(0, neighbor)
                return True

        return False
    
    def findAugmentingPath(self, apply = False):

        source = self.findSource()
        sink = self.findSink()

        path = []
        edges = []

        if self.hasPathToSink(source, path):

            currentNode = source
            # path.insert(0, source)

            maxCapacity = -1

            while len(path) > 0:
                # print("%s => %s" % (currentNode.letter, path[0].letter))
                edge = self.getEdge(currentNode, path[0])

                edges.append(edge)

                if maxCapacity == -1 or edge.capacity - edge.flow < maxCapacity:
                    maxCapacity = edge.capacity - edge.flow

                # print(currentNode.letter)
                # print(maxCapacity)
                currentNode = path.pop(0)

            if apply:

                self.augmentingPath = None

                for edge in edges:
                    edge.flow += maxCapacity

            else:
                
                self.augmentingPath = edges


        else:
            self.noMorePaths = True
        # done = False
        # currentNode = source

        # openNodes = []
        # closeNodes = []

        # while done == False:

        #     openNodes += self.getNeighbors(currentNode)

        #     for node in openNodes:
        #         if (hasPathToSink(node))



    def update(self):

        if (self.stateCounter % 2 == 1):
            self.findAugmentingPath()
            return
        
        if (self.stateCounter % 2 == 0):
            self.findAugmentingPath(True)
            return

        

class Node:

    isSource = False
    isSink = False
    letter = "A"
    x = None
    y = None
    
    neighbors = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
  
    def draw(self):
        noStroke()

        fill(29,134,152)
        ellipse(self.x, self.y, 40, 40)
        textSize(16)
        textAlign(CENTER, CENTER)
        fill(255)
        text(self.letter, self.x, self.y - 3); 
        

        

class Edge:
    

    flow = 0

    source = None
    target = None
    capacity = 0
    
    def __init__(self, source, target, capacity):
        self.source = source
        self.target = target
        self.capacity = capacity
    
    def draw(self, showFlow, showResidual, showCapacity):

        source = Node(self.source.x, self.source.y)
        target = Node(self.target.x, self.target.y)

        stroke(120)
        fill(120)

        if showCapacity and self.capacity > 0:
            drawArrow(source, target, 4)

            x = abs(self.source.x - self.target.x) / 2 + min(self.source.x, self.target.x)
            y = abs(self.source.y - self.target.y) / 2 + min(self.source.y, self.target.y)

            noStroke()
            fill(120)
            ellipse(x, y, 20, 20)

            textAlign(CENTER, CENTER)
            fill(200)
            text(self.capacity, x, y-2); 

 

        if showFlow and self.flow > 0:
            x = abs(self.source.x - self.target.x) / 2 + min(self.source.x, self.target.x)
            y = abs(self.source.y - self.target.y) / 2 + min(self.source.y, self.target.y)

            source = Node(self.source.x + 10, self.source.y + 10)
            target = Node(self.target.x + 10, self.target.y + 10)
            stroke	(230)
            fill	(230)
            drawArrow(source, target, 4)

            ellipse(x + 10, y + 10, 20, 20)
            textAlign(CENTER, CENTER)
            fill(70)
            text(self.flow, x + 10, y + 10); 


        if showResidual and self.flow > 0:

            x = abs(self.source.x - self.target.x) / 2 + min(self.source.x, self.target.x)
            y = abs(self.source.y - self.target.y) / 2 + min(self.source.y, self.target.y)

            source = Node(self.source.x - 10, self.source.y - 10)
            target = Node(self.target.x - 10, self.target.y - 10)
            stroke	(180, 100, 100)
            fill	(180, 100, 100)

            drawArrow(target, source, 4)

            ellipse(x - 10, y - 10, 20, 20)
            textAlign(CENTER, CENTER)
            fill(255)
            text(self.flow, x - 10, y - 10); 

            

        # stroke(150)
        # strokeWeight(4)
        # line(self.source.x, self.source.y, self.self.target.x, self.self.target.y)

        # textSize(12)

            

    





    # def drawAsArrow(self):

       

        # a = 3 #dist(x1, y1, x2, y2) / 50

        # source = Node(self.source.x + 5, self.source.y + 5)
        # target = Node(self.target.x + 5, self.target.y + 5)

        # dx = source.x - target.x
        # dy = source.y - target.y

        # pushMatrix()
        # translate(target.x + 0.9 * dx, target.y + 0.9 * dy)
        # rotate(atan2(dy, dx))
        # triangle(- a * 2 , - a, 0, 0, - a * 2, a)
        # popMatrix()
        # line(target.x + 0.1 * dx,  target.y + 0.1 * dy, target.x + 0.9 * dx,  target.y + 0.9 * dy)  







