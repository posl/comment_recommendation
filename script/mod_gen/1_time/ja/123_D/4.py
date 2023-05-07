def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse = True)
    AB = AB[:K]
    
    ABC = []
    for ab in AB:
        for c in C:
            ABC.append(ab + c)
    ABC.sort(reverse = True)
    ABC = ABC[:K]
    
    for abc in ABC:
        print(abc)

if __name__ == '__main__':
    main()