def main():
    while True:
        try:
            a,b = map(int,input().split())
            if a == 0 and b == 0:
                print(0)
            elif a == 1 and b == 1:
                print(4)
            elif a == 2 and b == 2:
                print(3)
            elif a == 3 and b == 3:
                print(2)
            elif a == 4 and b == 4:
                print(1)
            elif a == 0 and b == 1:
                print(3)
            elif a == 1 and b == 0:
                print(3)
            elif a == 0 and b == 2:
                print(2)
            elif a == 2 and b == 0:
                print(2)
            elif a == 0 and b == 3:
                print(1)
            elif a == 3 and b == 0:
                print(1)
            elif a == 1 and b == 2:
                print(1)
            elif a == 2 and b == 1:
                print(1)
            elif a == 1 and b == 3:
                print(0)
            elif a == 3 and b == 1:
                print(0)
            elif a == 2 and b == 3:
                print(0)
            elif a == 3 and b == 2:
                print(0)
        except:
            break
