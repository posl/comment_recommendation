def main():
    n,m = map(int, input().split())
    x = []
    for _ in range(m):
        x.append(list(map(int, input().split()))[1:])
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(m):
                if not (i+1 in x[k] and j+1 in x[k]):
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

if __name__ == '__main__':
    main()