cs= "a=b;c=d;e=f;g=h"
def cstolot(cs):
    lot = []
    for i in cs.split(";"):
        lot.append(tuple(i.split("=")))
    print(lot)
cstolot(cs)