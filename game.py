from os import system


class Hangman:
    def __init__(self):
        self.array = []
        self.dead = 5
        self.index = 0
        self.next = ""
        system("cls")
        system("color d")
        print("""
                    X      X  XXXXXXX  XX    X  XXXXXXXX  XX    XX  XXXXXXX  xx    x
                    X      X  X     X  X X   X  X         X X  X X  x     x  x x   x
                    XXXXXXXX  XXXXXXX  X  X  X  X   XXXX  X  XX  X  xxxxxxx  x  x  x
                    X      X  X     X  X   X X  X      X  X      X  x     x  x   x x
                    X      X  X     X  X    XX  XXXXXXXX  X      X  x     x  x    xx
        """)
        self.laodfile()

    def laodfile(self):
        file = open("hangman.txt", encoding="utf-8")
        files = ""
        while True:
            files = file.readline()
            if files == "":
                break
            else:
                self.array.append(files)
        file.close()
        self.getword()
        self.start()
    def getword(self):
        self.key = ""
        self.dead = 5
        if self.index < len(self.array):
            self.word = self.array[self.index]
            self.next = (len(self.word)-1)*' _'
            self.index += 1
            system("cls")
        else:
            print("game over!")
            exit()
    def start(self):
        print(self.next)
        print(f"dead:{self.dead}    words:{self.key}")
        self.answer = input("key:").lower()
        self.key += self.answer
        self.control()
    def control(self):
        i = 0
        ok = True
        win = True
        _list = list(self.next)
        while i < len(self.next):
            if self.word[i-1:i] == self.answer:
                _list[i*2-1:i*2] = self.answer
                ok = False
            if self.next[i-1:i] == '_':
                win = False
            i += 1

        if ok:
            self.dead -= 1
            if self.dead == 0:
                print("game over!")
                exit()
        if win:
            self.getword()
            self.start()
        else:
            self.next = "".join(_list)
            self.start()


# main function start
if __name__ == "__main__":
    Hangman()
