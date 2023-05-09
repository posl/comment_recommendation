def main():
    k = int(input())
    print("22:0{0}".format(k%60) if k%60 < 10 else "22:{0}".format(k%60))
