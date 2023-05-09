def main():
    N = int(input())
    S = set()
    for i in range(1, 2*N+2):
        S.add(i)
    for i in range(1, 2*N+2):
        print(i)
        S.remove(i)
        if i%2==0:
            a = int(input())
            if a == 0:
                return
            S.remove(a)
    return

if __name__ == '__main__':
    main()