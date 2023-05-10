def main():
    q = int(input())
    a = []
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            a.append(int(query[1]))
        elif query[0] == "2":
            x = int(query[1])
            k = int(query[2])
            b = [i for i in a if i <= x]
            if len(b) < k:
                print(-1)
            else:
                print(sorted(b)[-k])
        elif query[0] == "3":
            x = int(query[1])
            k = int(query[2])
            b = [i for i in a if i >= x]
            if len(b) < k:
                print(-1)
            else:
                print(sorted(b)[k-1])
