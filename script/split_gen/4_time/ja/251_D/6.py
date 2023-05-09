def main():
    w = int(input())
    if w == 3:
        print(2)
        print(1,2)
    else:
        print(3)
        if w % 2 == 0:
            print(w//2,w//2,1)
        else:
            print(w//2,w//2+1,1)
