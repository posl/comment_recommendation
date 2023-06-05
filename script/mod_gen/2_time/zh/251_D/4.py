def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = input().split()
        S.append(s)
        T.append(int(t))
    max = 0
    max_index = 0
    for i in range(N):
        if T[i] > max:
            max = T[i]
            max_index = i
    print(max_index+1)
    return

if __name__ == '__main__':
    main()