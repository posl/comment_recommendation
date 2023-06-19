def main():
    n = int(input())
    A = []
    for i in range(n):
        query = input().split()
        if query[0] == "1":
            A.append(int(query[1]))
        elif query[0] == "2":
            x = int(query[1])
            k = int(query[2])
            count = 0
            for a in A:
                if x >= a:
                    count += 1
            if count >= k:
                print(sorted(A, reverse=True)[k-1])
            else:
                print("-1")
        elif query[0] == "3":
            x = int(query[1])
            k = int(query[2])
            count = 0
            for a in A:
                if x <= a:
                    count += 1
            if count >= k:
                print(sorted(A)[k-1])
            else:
                print("-1")

if __name__ == '__main__':
    main()