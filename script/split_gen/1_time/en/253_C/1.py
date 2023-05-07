def main():
    Q = int(input())
    S = []
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            S.append(int(query[1]))
        elif query[0] == '2':
            S = [x for x in S if x != int(query[1])]
        else:
            print(max(S) - min(S))
