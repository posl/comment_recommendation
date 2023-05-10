def main():
    N = int(input())
    S = []
    for i in range(N):
        query = input().split()
        if query[0] == '1':
            S.append(int(query[1]))
        elif query[0] == '2':
            x, c = int(query[1]), int(query[2])
            for j in range(min(c, S.count(x))):
                S.remove(x)
        else:
            print(max(S) - min(S))
