import random
import csv
import math


# Here I created a neural network from scratch and used a quasi-genetic selection process to train the weigts of the model 

class Model:
    def __init__(self, layers):
        # the layers are essentially the model since they are all of the
        # weights
        self.layers = layers
    # no comment here
    def eval(self, input):
        result = input
        for layer in self.layers:
            result = layer.eval(result)
        return result
    # we all know what this does
    def train(self, trainingDataPath):
        trainingData = []
        with open(trainingDataPath, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                trainingDataRow = []
                for i in range(1, 601):
                    if(row[i] == ""):
                        trainingDataRow.append(0)
                    else:
                        trainingDataRow.append(float(row[i]))
                trainingData.append(trainingDataRow)
        i = 0
        batchsize = 5
        while(i<100):
            batch = []
            currInd = i
            while(i<len(trainingData) and i<currInd+batchsize):
                batch.append(trainingData[i])
                i=i+1
            print(len(batch))
            self.errorCorrection(batch)
            print("finished epoch:"+str(i))
            i=i+1
        return self.layers

    # Think this is pretty self explanatory
    def randWeightsCreator(self, trueWeights, newWeightsCount, changesPerWeights):
        allNewWeights = []
        for i in range(0,newWeightsCount):
            newWeights = trueWeights.copy()
            for i in range(0,changesPerWeights):
                weightIndex = random.randint(0, len(newWeights)-1)
                weight = random.random()
                newWeights[weightIndex] = weight
            allNewWeights.append(newWeights)
        return allNewWeights

    # backpropagates and adjusts weights at each step
    def errorCorrection(self, batch):

        input = batch[0:300]
        output = batch[301:600]
        for i in reversed(range(0,len(self.layers))):
            layer = self.layers[i]
            # creates a bunch of new weights with some number of random changes to them, and then takes the best one (minimum loss)
            # I couldnt think of anything better lol
            newWeights = self.randWeightsCreator(self.layers[i].weights, 1,1)
            minLoss = 99999999999
            bestWeight = newWeights[0]
            for weights in newWeights:
                newLoss =minLoss = self.negLogLoss(batch)
                if newLoss < minLoss :
                    minLoss = newLoss
                    bestWeight = weights
            self.layers[i].weights = bestWeight
        

    
    # negative log likelyhood loss function given for the competion
    def negLogLoss(self, batch):
        preLoglossSum = 0

        
        for data in batch:
            input = data[0:300]
            trueOutput = data[301:600]
            modelOutput = self.eval(input)
            
            ei = []
            for i in range(0,len(trueOutput)):
                ei.append(trueOutput[i]-modelOutput[i])
            EiG = 0
            for i in range(0,len(trueOutput)):
                CovMatApprox = 0
                if i <= 60:
                    CovMatApprox = math.exp(math.log(i+1)*1.0406028049510443 - 6.430669850650689)
                elif i<=244:
                    CovMatApprox = math.exp(-1*2.1617411566043896)
                else:
                    CovMatApprox = math.exp(math.log(i+1)*7.835345062351012 + -45.24876794412965)


                EiG += ei[i]*(ei[i]*CovMatApprox)

            preLoglossSum+=(1/len(batch))*EiG

        return -1*math.log(preLoglossSum)
            
            
        

    # Mean squared loss made as a place holder loss function while I was developing this

    def meanSquaredLoss(self,modelOutput,realOutput):
        totalLoss = 0
        for i in range(0,len(realOutput)):
            totalLoss+=(modelOutput[i]-realOutput[i])*(modelOutput[i]-realOutput[i])
        return totalLoss
        

# each layer has a list of weights that controls the influence of certain nuerons in the input
class Layer:
    def __init__(self, size):
        self.size = size
        self.weights = []
        for i in range(0,size):
            self.weights.append(1)

    # the outputs are simply just sums of the product of the weigths
    def eval(self, input):
        output = []
        for i in range(0,self.size):
            output.append(0)
        for neuron in input:
            for i in range(0,len(self.weights)):
                output[i] += self.weights[i]*neuron
        return output


def makeEmptyModel(layersCount):
    layers = []
    for i in range(0,layersCount):
        num = random.randint(300, 1000)
        layers.append(Layer(num))
    layers.append(Layer(300))
    return Model(layers)


# execution of creating the model
layersCount = 1
model = makeEmptyModel(layersCount)
model.train("train.csv")

weights = []
for layer in model.layers:
    weights.append(layer.weights)

with open("weights.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(weights)
