def main():
    N, M = map(int, input().split())
    K = []
    for i in range(M):
        K.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(M):
                if not (i+1 in K[k][1:] and j+1 in K[k][1:]):
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print("Yes")
        return
    print("No")
    return

if __name__ == '__main__':
    main()