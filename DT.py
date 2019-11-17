class Tree(object):
    def set_leaf(self):
        self.is_leaf=True
    def check_leaf(self):
        return self.is_leaf
    def set_class(self,v):
        self.c=v

    def set_node_value(self,v):
        self.value=v

    def set_instances(self,g):
        self.instaces=g

    def __init__(self,h):
        self.dict = {}
        self.height = h
        self.is_leaf=False
        self.value=0
        self.c=0

class DecisionTree():
    def predict(self,testfile):
        v=self.pd.read_csv(testfile,sep=', ',header=None)
        p=self.np.array(v)
        for i in p:
            # print i
            self.check_trav(self.t,i)
        print self.l
        print "Accuracy: ",(self.cor*100.0)/(self.wor+self.cor)

    def check_trav(self,t,X):
        if t.check_leaf()==True:
            if t.c==X[14]:
                self.cor=self.cor+1
            else:
                self.wor = self.wor + 1
            self.l.append(t.c)
        else:
            value=X[t.value]
            if value in t.dict:
                self.check_trav(t.dict[value],X)
            else:
                if t.c == X[14]:
                    self.cor = self.cor + 1
                else:
                    self.wor = self.wor + 1
                self.l.append(t.c)

    def train(self,trainfile):
        X=self.pd.read_csv(trainfile, sep=', ',header=None)
        r,c=self.np.shape(X)
        df = self.pd.DataFrame(X)
        self.t=self.generate_dt(df,0,[1,3,5,6,7,8,9,13])

    def generate_dt(self,X,h,attributes):
        # print attributes
        t=Tree(h)
        t.set_instances(len(X))
        g=self.get_groups(X,[14])
        if len(attributes)>2:
            if len(g[0])>len(g[1]):
                t.set_class(0)
            else:
                t.set_class(1)
        # print len(g.groups)
        if len(g.groups)<=1:
            l=g.groups
            l=l.keys()[0]
            t.set_class(l)
            t.set_leaf()
            # print "leaf"
        elif len(attributes)<=2:
            if len(g[0])>len(g[1]):
                t.set_leaf()
                t.set_class(0)
                # print "leaf 0"
            else:
                t.set_leaf()
                t.set_class(1)
                # print "leaf 1"
        else:
            min=self.find_min_entropy(X,attributes)
            g=self.get_groups(X,[attributes[min]])
            t.set_node_value(attributes[min])
            # attributes.remove(attributes[min])
            pp=[]
            for i in attributes:
                if i is not attributes[min]:
                    pp.append(i)
            for i in g.groups:
                df=g.get_group(i)
                # print i
                df=df.values
                df =self.pd.DataFrame(df)
                p=self.generate_dt(df, h + 1, pp)
                t.dict[str(i)]=p
            # print
        return t

    def get_groups(self,df,set):
        g = df.groupby(set)
        return g
        pass

    def find_min_entropy(self,X,attributes):
            min_ent = []
            for i in attributes:
                min_ent.append(self.calculate_entropy(X, i))
            index, value = max(enumerate(min_ent), key=self.op.itemgetter(1))
            # print min_ent
            return index

    def calculate_entropy(self,X,i):
        if type(X[i][0]) in [self.np.int64,self.np.int64]:
            return -9999
            pass
        else:
            g = self.get_groups(X,[i])
            entropy = 0
            for gi in g.groups:
                noofcat = len(g.groups[gi])
                sg = g.get_group(gi)
                sg = self.pd.DataFrame(sg)
                subg = self.get_groups(sg,[i, 14])
                PB = noofcat / float(10000)
                class_ent = 0
                for subgi in subg.groups:
                    noofcatp = len(subg.groups[subgi])
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
        from types import IntType as inttype
        import pandas as pdtype
        import numpy
        import math
        import operator
        self.np=numpy
        self.pd = pdtype
        self.mt=math
        self.op=operator
        self.inttype=inttype
        self.l = []
        self.cor = 0
        self.wor = 0
        self.t=""
        pass


model=DecisionTree()
model.train("train.csv")
model.print_tree()
model.predict("test.csv")
#
#
# import pickle
#
# class account:
#     def __init__(self, id, balance):
#         import numpy
#         self.np=numpy
#         self.id = id
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         self.balance -= amount
#
# myac = account('123', 100)
# myac.deposit(800)
# myac.withdraw(500)
#
# fd = open( "archive", "wb" )
# pickle.dump( myac, fd)
# fd.close()
#
# # import pickle
# # with open('cse.model', 'wb') as f:
# #     pickle.dump(model, f)
#
# # f=open('cs17mtech11004.model','r')
# # mod=pickle.load(f)x`
#
