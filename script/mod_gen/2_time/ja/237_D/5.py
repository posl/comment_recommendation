def main():
    N = int(input())
    S = input()
    L = []
    R = []
    for i in range(N):
        if S[i] == "L":
            L.append(i)
        else:
            R.append(i)
    A = [0]
    for i in range(N):
        if S[i] == "L":
            if len(L) > 0:
                A.insert(L[0], i+1)
                L.pop(0)
        else:
            if len(R) > 0:
                A.insert(R[0]+1, i+1)
                R.pop(0)
    print(*A)

if __name__ == '__main__':
    main()