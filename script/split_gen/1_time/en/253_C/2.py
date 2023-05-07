def main():
    q = int(input())
    s = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s.append(query[1])
        elif query[0] == 2:
            for _ in range(min(query[2], s.count(query[1]))):
                s.remove(query[1])
        elif query[0] == 3:
            print(max(s) - min(s))
