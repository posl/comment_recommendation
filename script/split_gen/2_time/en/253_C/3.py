def main():
    Q = int(input())
    S = []
    for i in range(Q):
        query = input()
        if query[0] == "1":
            S.append(int(query[2:]))
        elif query[0] == "2":
            query = query.split(" ")
            x = int(query[1])
            c = int(query[2])
            for j in range(min(c,S.count(x))):
                S.remove(x)
        elif query[0] == "3":
            print(max(S)-min(S))
