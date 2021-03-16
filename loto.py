import random
from os import system
class Loto:
    def __init__(self) -> None:
        system("cls")
        self.key=[]
        self._loto=[]
        self.start()
    def start(self):
        for i in range(0,10):
            self.key.append(str(random.randint(0, 20)))
        self.loto()
    def loto(self):
        for i in range(0,10):
            self._loto.append(input("key:"))
        self.result()
    def result(self):
        win=0
        print(self.key)
        print(self._loto)
        i=0
        while i< len(self.key):
            j=0
            while j<len(self.key):
                if self.key[i]==self._loto[j]:
                    win+=1
                j+=1
            i+=1
        print(f"score:%{win*100/20}")


        
















if __name__=="__main__":
    Loto()
