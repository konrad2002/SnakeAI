# example code for a neural network

import numpy as np
import random
from sklearn.utils.validation import check_random_state

class AiAnnExample (object):
    def __init__ (  self,
                    nNeurons = [1, 1, 1],
                    weights = None,
                    activationF = ["sigmoid"],
                    outputF = ["id"]
                ):

        print("[ai  ] created " + str(self.__class__))

        self.nNeurons = nNeurons

        self.activationF = activationF
        self.outputF = outputF

        self.randomInt = random.randint(10, 50)
        self.random_state_ = check_random_state(self.randomInt)


        self.network = []
        self.layers = []
        self.weights = []

        for layer,neurons in enumerate(self.nNeurons):

            # init neurons of layer with 0
            self.layers.append(
                np.zeros((neurons + 1, 5))
            )

            self.layers[layer][0,:] = 1


            if not weights:
                # init weights between layer and next layer with 0
                if layer < ( len(self.nNeurons) - 1 ):
                    self.weights.append(
                        4 * self.random_state_.random_sample((neurons + 1, self.nNeurons[layer + 1] + 1)) - 2
                        # np.ones((neurons + 1, self.nNeurons[layer + 1] + 1))
                    )


        if weights:
            self.weights = weights

    def function(self, fType, x):

        # used for activation functions and output functions

        y = []

        if not fType:
            fType = "heaviside"

        if fType == "heaviside":
            for X in x:
                if X >= 0:
                    y.append(1)
                else:
                    y.append(0)

        elif fType == "sigmoid":
            y = 1 / ( 1 + np.exp(-x) )

        elif fType == "relu":
            y = np.maximum(0, x)

        elif fType == "id":
            y = x


        return y


    def predict(self, x):

        self.layers[0][1:,2] = x

        for i,layer in enumerate(self.layers):
            if i > 0:
                layer[1:,0] = np.dot(self.layers[i - 1][:,2], self.weights[i - 1][:,1:])

                # print("")
                # print(self.layers[i - 1][:,2])
                # print("dot")
                # print(self.weights[i - 1][:,1:])
                # print("equals")
                # print(layer[1:,0])
                # print("")

                layer[1:,1] = self.function(self.activationF[i - 1], layer[1:,0])

                layer[1:,2] = self.function(self.outputF[i - 1], layer[1:,1])

        output = self.layers[len(self.nNeurons) - 1][:,2]

        return output


    def direction(self, sensorData):

        x = []
        print("data  : " + str(sensorData))

        for data in sensorData:
            for subdata in data:
                x.append(subdata)

        print("input : " + str(x))

        output = self.predict(x)

        print("output: " + str(output))

        maximum = 0
        newDirection = 0
        for i,a in enumerate(output):
            if a > maximum:
                maximum = a
                newDirection = i

        print("direct: " + str(newDirection))
        print("")
        return newDirection


    def printNetwork(self):

        print("weights")
        print(self.weights)
        print("")

        for i,layer in enumerate(self.layers):
            print("[Layer  " + str(i) + "]: ")
            print(layer)

            if i < ( len(self.weights) ):
                print("[Weight " + str(i) + "]: ")
                print(self.weights[i])


        for i,layer in enumerate(self.layers):

            row = ""
            ro2 = ""
            for _ in range(self.nNeurons[i]):
                row += " O "
                ro2 += " | "

            print("")
            if i > 0:
                print(ro2)
            print(row)
            if i < ( len(self.weights) ):
                print(ro2)
            print("")

            if i < ( len(self.weights) ):
                print(" " + str(self.nNeurons[i]) + "x" + str(self.nNeurons[i + 1]) + " weights")


weights = []

weights.append(
    np.matrix(
        [
            [0,-2],
            [0,1],
            [0,1]
        ]
    )
)


ai = AiAnnExample([2, 1], weights=weights, activationF=["heaviside","heaviside"], outputF=["id", "id"])
ai.printNetwork()

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
for x in X:
    output = ai.predict(x)

print("")
print("")
print("output:")
print(output)
print("")
print("")

ai.printNetwork()