import csv
import numpy as np


class Tree(object):
    def set_leaf(self):
        self.is_leaf = True

    def check_leaf(self):
        return self.is_leaf

    def set_class(self, v):
        self.c = v

    def set_node_value(self, v):
        self.value = v

    def set_instances(self, g):
        self.instaces = g

    def __init__(self, h):
        self.dict = {}
        self.height = h
        self.is_leaf = False
        self.value = 0
        self.c = 0


class DecisionTree():
    def predict(self, testfile):
        f = open(testfile, 'rb')
        reader = csv.reader((line.replace(', ', ',') for line in f), delimiter=',')
        X = list(reader)
        p = self.np.array(X)
        for i in p:
            self.check_trav(self.t, i)
        print "Accuracy: ", (self.cor * 100.0) / (self.wor + self.cor)

    def check_trav(self, t, X):
        if t.check_leaf() == True:
            if t.c == int(X[14]):
                self.cor = self.cor + 1
            else:
                self.wor = self.wor + 1
            self.l.append(t.c)
        else:
            value = X[t.value]
            if value in t.dict:
                self.check_trav(t.dict[value], X)
            else:
                if t.c == int(X[14]):
                    self.cor = self.cor + 1
                else:
                    self.wor = self.wor + 1
                self.l.append(t.c)

    def train(self, trainfile):
        f = open(trainfile, 'rb')
        reader = csv.reader((line.replace(', ', ',') for line in f), delimiter=',')
        X = list(reader)
        r, c = np.shape(X)
        X = np.array(X)
        self.t = self.generate_dt(X, 0, [1, 3, 5, 6, 7, 8, 9, 13])

    def get_groups(self, d, attr):
        dict = {}
        x = set(d[:, attr[0]])
        for i in x:
            dict[i] = []
        for i in d:
            dict[i[attr[0]]].append(np.array(i))
        return dict

    def get_groups_for_two(self,d,attr):
        dict=self.get_groups(d,[14])
        dict2={}
        x=set(d[:,attr[0]])
        for i in dict.keys():
            for j in x:
                dict2[j+" "+i]=[]
        for i in dict.keys():
            for j in dict[i]:
                p=j[attr[0]]+" "+i
                dict2[p].append(j)
        return dict2

    def generate_dt(self, X, h, attributes):
        t = Tree(h)
        g = self.get_groups(X, [14])
        if len(attributes) > 2 and len(g.keys()) > 1 :
            if len(g['0']) > len(g['1']):
                t.set_class(0)
            else:
                t.set_class(1)
        # print len(g.groups)
        if len(g.keys()) <= 1:
            l = g.keys()[0]
            t.set_class(int(l))
            t.set_leaf()
            # print "leaf"
        elif len(attributes) <= 2:
            if len(g['0']) > len(g['1']):
                t.set_leaf()
                t.set_class(0)
                # print "leaf 0"
            else:
                t.set_leaf()
                t.set_class(1)
                # print "leaf 1"
        else:
            min = self.find_min_entropy(X, attributes)
            g = self.get_groups(X, [attributes[min]])
            t.set_node_value(attributes[min])
            # attributes.remove(attributes[min])
            pp = []
            for i in attributes:
                if i is not attributes[min]:
                    pp.append(i)
            for i in g.keys():
                df = g[i]
                df=np.array(df)
                p = self.generate_dt(df, h + 1, pp)
                t.dict[str(i)] = p
        return t

    def find_min_entropy(self, X, attributes):
        min_ent = []
        for i in attributes:
            min_ent.append(self.calculate_entropy(X, i))
        index, value = max(enumerate(min_ent), key=self.op.itemgetter(1))
        return index

    def calculate_entropy(self, X, i):
        l=X[0][i]
        if type(X[0][i]) in [self.np.int64, self.np.int64]:
            return -9999
            pass
        else:
            g = self.get_groups(X, [i])
            entropy = 0
            for gi in g.keys():
                noofcat = len(g[gi])
                sg = np.array(g[gi])
                subg = self.get_groups_for_two(sg,[i])
                PB = noofcat / float(10000)
                class_ent = 0
                for subgi in subg.keys():
                    noofcatp = len(subg[subgi])
                    prob = noofcatp / float(noofcat)
                    class_ent = class_ent + prob * self.mt.log(prob, 2)
                PB = PB * class_ent
                entropy = entropy + PB
            # print i,entropy
            return entropy
            pass

    def print_tree(self):
        self.pretty(self.t)

    def pretty(self,t, indent=0):
        if t.check_leaf()==True:
            print '\t' * indent*2,t.c
        else:
            for i in t.dict:
                print '\t' * indent*2,t.value,i
                self.pretty(t.dict[i],indent+1)

    def __init__(self):
        import numpy
        import math
        import operator
        self.op=operator
        self.np = numpy
        self.mt= math
        self.l = []
        self.cor = 0
        self.wor = 0

model = DecisionTree()
model.train("train1.csv")
model.print_tree()
model.predict("test.csv")