from graph import *
from graph_generator import *

graph = None

def setup():
    global graph
   

    size(800, 800)
    fill(40)
    stroke(40)
    strokeWeight(2)

    textFont(createFont("Courier New Bold", 14))

    graph = GraphGenerator.create(10)

    # for i in range(20):
    #     drawArrow(random(800), random(800), random(800), random(800))

    


def mousePressed():
    global graph

    graph.stateCounter += 1
    graph.update()
    # graph.findAugmentingPath()

def keyPressed():
    global graph

    if key == "w":
        graph.showResidual = not graph.showResidual

    if key == "q":
        graph.showCapacity = not graph.showCapacity

    if key == "e":
        graph.showFlow = not graph.showFlow

def draw():
   global graph
   background(180, 255)
   graph.draw()

   