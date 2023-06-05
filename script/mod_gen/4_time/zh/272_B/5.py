def main():
    n,m = map(int,input().split())
    k = [0 for i in range(m)]
    x = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        k[i],*x[i] = map(int,input().split())
    for i in range(n):
        for j in range(n):
            if i != j:
                flag = 0
                for l in range(m):
                    if i+1 in x[l] and j+1 in x[l]:
                        flag = 1
                        break
                if flag == 0:
                    print("No")
                    return
    print("Yes")
    return

if __name__ == '__main__':
    main()