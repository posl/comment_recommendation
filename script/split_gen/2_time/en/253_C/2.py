def main():
    Q = int(input())
    S = []
    for q in range(Q):
        query = input().split()
        if query[0] == "1":
            S.append(int(query[1]))
        elif query[0] == "2":
            m = min(int(query[2]), S.count(int(query[1])))
            for i in range(m):
                S.remove(int(query[1]))
        else:
            print(max(S)-min(S))
