def main():
    N = int(input())
    dic = {}
    for i in range(N):
        S, T = input().split()
        T = int(T)
        if S not in dic:
            dic[S] = T
        else:
            dic[S] = max(dic[S], T)
    max_val = max(dic.values())
    for i in range(N):
        S, T = input().split()
        T = int(T)
        if S in dic and dic[S] == max_val:
            print(i+1)
            break

if __name__ == '__main__':
    main()