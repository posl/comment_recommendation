def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = int(input())
    print(a)
    q = int(input())
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            a.append(int(query[1]))
        else:
            x = int(query[1])
            k = int(query[2])
            if query[0] == "2":
                cnt = 0
                for j in range(len(a)):
                    if a[j] <= x:
                        cnt += 1
                        if cnt == k:
                            print(a[j])
                            break
                else:
                    print(-1)
            else:
                cnt = 0
                for j in range(len(a)):
                    if a[j] >= x:
                        cnt += 1
                        if cnt == k:
                            print(a[j])
                            break
                else:
                    print(-1)

if __name__ == '__main__':
    main()