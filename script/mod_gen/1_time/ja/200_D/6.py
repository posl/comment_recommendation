def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    modA = [a % mod for a in A]
    modA_set = set(modA)
    if len(modA_set) == N:
        print("No")
        return
    print("Yes")
    modA_dict = {}
    for i, a in enumerate(modA):
        if a in modA_dict:
            modA_dict[a].append(i+1)
        else:
            modA_dict[a] = [i+1]
    for a in modA_dict:
        if len(modA_dict[a]) > 1:
            x = len(modA_dict[a])
            print(x, *modA_dict[a])
            break
    y = N - x
    C = []
    for i in range(N):
        if i+1 not in modA_dict[a]:
            C.append(i+1)
    print(y, *C)
main()

if __name__ == '__main__':
    main()