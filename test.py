import dill
fl=open('cs17mtech11004.model','rb')
l=dill.load(fl)
l.predict("Trash/test.csv")
