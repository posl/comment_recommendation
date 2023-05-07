def main():
    S = input()
    Q = int(input())
    query = [list(map(str, input().split())) for _ in range(Q)]
    ans = []
    for i in range(Q):
        if query[i][0] == '1':
            S = S[::-1]
        elif query[i][0] == '2':
            if query[i][1] == '1':
                S = query[i][2] + S
            elif query[i][1] == '2':
                S = S + query[i][2]
    print(S)
