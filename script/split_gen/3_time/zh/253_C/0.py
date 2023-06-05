def main():
    n = int(input())
    s = []
    for i in range(n):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s.append(query[1])
        elif query[0] == 2:
            for j in range(query[2]):
                if query[1] in s:
                    s.remove(query[1])
        elif query[0] == 3:
            print(max(s)-min(s))
