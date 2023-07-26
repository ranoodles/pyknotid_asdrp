import numpy as np
from pyknotid.make import torus_knot
from pyknotid.make import figure_eight
from matplotlib import pyplot as plt
import csv

class myKnot():
    def __init__(self, k, name):
        self.knot = k
        self.k_name = name
    
    def display(self):
        x_ints=[i[0] for i in self.knot.points]
        y_ints=[i[1] for i in self.knot.points]
        z_ints=[i[2] for i in self.knot.points]
        ax = plt.axes(projection='3d')
        ax.scatter(x_ints,y_ints,z_ints, cmap=plt.cm.Spectral)
        plt.show()

    def create_csv(self):
        with open(self.k_name+".csv", mode="w") as csv_file:
            fieldnames = ["x","y","z"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for point in self.knot.points:
                writer.writerow({"x":point[0], "y":point[1], "z":point[2]})

figureeight = myKnot(torus_knot(2,3), "torus_2_3")
# figureeight.display()
figureeight.create_csv()

