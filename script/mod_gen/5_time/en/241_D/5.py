def main():
    N = int(input())
    A = []
    for i in range(N):
        query = input().split()
        if query[0] == '1':
            A.append(int(query[1]))
        else:
            x = int(query[1])
            k = int(query[2])
            if query[0] == '2':
                B = [a for a in A if a <= x]
                if len(B) < k:
                    print(-1)
                else:
                    print(sorted(B)[-k])
            else:
                B = [a for a in A if a >= x]
                if len(B) < k:
                    print(-1)
                else:
                    print(sorted(B)[k-1])

if __name__ == '__main__':
    main()