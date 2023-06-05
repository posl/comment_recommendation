def main():
    A,B,C,D,E,F,X = map(int,input().split())
    t = 0
    while True:
        if t % (A+B) < A:
            X -= E
        else:
            X -= F
        if X <= 0:
            print("高桥" if t % (A+B) < A else "青木")
            break
        if t % (C+D) < C:
            X -= E
        else:
            X -= F
        if X <= 0:
            print("高桥" if t % (C+D) < C else "青木")
            break
        t += 1
main()
