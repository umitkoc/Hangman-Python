# En az bir büyük harf, en az bir küçük harf, en az 8 karakter alfanumerik bir şifre oluşturma politikasına göre rastgele şifre üreten bir program yazınız.
# Rastgele şifreler belirleyerek yada üreterek 1.maddede ki kriterlere uymayan şifreleri belirleyiniz
import random
from os import system


class Password:
    def __init__(self,again):
        self.character = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890"
        self.array = []
        self.again=again
        self.passwords()

    def start(self):
        _password = ""
        num = random.randint(1, 62)
        for i in range(num):
            rnd = random.randint(0, 62)
            _password += self.character[rnd-1:rnd]
        self.array.append(_password)
        return _password

    def passwords(self):
        self.file = open("password.txt", "w", encoding="utf-8")
        for i in range(self.again):
            self.file.write(f"{self.start()} \n")
        self.control()

    def control(self):
        self.file.write("\n\n\nhatalar\n\n\n")
        for i in self.array:
            if len(i) < 8:
                self.file.write(f"{i} :8 karakterden küçük \n")
            else:
                i = str(i)
                small = self.sml(i)
                large = self.lrg(i)
                result = large and small
                if not result:
                    self.file.write(f"{i} :küççük büyük hatası \n")
        self.openfile()

    def sml(self, i):
        for item in i:
            if item.islower():
                return True
        return False

    def lrg(self, i):
        for item in i:
            if item.isupper():
                return True
        return False

    def openfile(self):
        self.file.close()
        system("start password.txt")


if __name__ == "__main__":
    Password(50)
