from twisted.conch.insults.colors import REVERSE
from types import *
import math
import operator
class Rules:
    def __init__(self,h):
        self.dict = []
        self.height = h
        self.is_leaf=False



class DecisionTree:
    def predict(self,testfile):
        self.pd.read_csv(testfile)

    def train(self,trainfile):
        X=data = self.pd.read_csv(trainfile, sep=', ',header=None)
        r,c=self.np.shape(X)
        df = self.pd.DataFrame(X)
        self.rec(df,0)

    def rec(self,X,h):
        if h>6:
           return
        else:
            min_ent = []
            for i in range(0, 14-h):
                min_ent.append(self.calculate_entropy(X, i,h))
            index, value = max(enumerate(min_ent), key=operator.itemgetter(1))
            df = self.pd.DataFrame(X)
            g=self.get_groups(df,[index])
            self.create_nodes()
            for i in g.groups:
                df=g.get_group(i)
                d=df.drop(index, axis=1)
                d=d.values
                df =self.pd.DataFrame(d)
                self.rec(df,h+1)
            pass

    def create_nodes(self):
        pass

    def get_groups(self,df,set):
        g = df.groupby(set)
        return g
        pass

    def calculate_entropy(self,X,i,h):
        if type(X[i][0]) in [self.np.int64,self.np.int64,IntType,FloatType]:
            return -9999
            pass
        else:
            g = self.get_groups(X,[i])
            entropy = 0
            for gi in g.groups:
                noofcat = len(g.groups[gi])
                sg = g.get_group(gi)
                sg = self.pd.DataFrame(sg)
                subg = self.get_groups(sg,[i, 14-h])
                PB = noofcat / float(10000)
                class_ent = 0
                for subgi in subg.groups:
                    noofcatp = len(subg.groups[subgi])
                    prob = noofcatp / float(noofcat)
                    class_ent = class_ent + prob * math.log(prob, 2)
                PB = PB * class_ent
                entropy = entropy + PB
            print i,entropy
            return entropy
            pass

    def __init__(self):
        import pandas
        import numpy
        self.np=numpy
        self.pd=pandas
        self.tree=Rules(0)

model=DecisionTree()
model.train("train.csv")
# model.test("train.csv")