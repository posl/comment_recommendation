def main():
    a,b,w = map(int,input().split())
    w *= 1000
    if w % b == 0:
        mini = w // b
    else:
        mini = w // b + 1
    if w % a == 0:
        maxi = w // a
    else:
        maxi = w // a + 1
    if mini <= maxi:
        print(mini,maxi)
    else:
        print("UNSATISFIABLE")

if __name__ == '__main__':
    main()