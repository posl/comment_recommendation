def main():
    N, M = map(int, input().split())
    a = []
    for i in range(M):
        a.append(list(map(int, input().split()))[1:])
    for i in range(N):
        for j in range(i+1, N):
            for k in range(M):
                if not (i+1 in a[k] and j+1 in a[k]):
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print("Yes")
        exit()
    print("No")

if __name__ == '__main__':
    main()