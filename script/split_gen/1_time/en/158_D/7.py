def main():
    S = input()
    Q = int(input())
    queries = [input().split() for _ in range(Q)]
    queries.reverse()
    rev = False
    for query in queries:
        if query[0] == '1':
            rev = not rev
        else:
            if (query[1] == '1') ^ rev:
                S = query[2] + S
            else:
                S = S + query[2]
    if rev:
        S = S[::-1]
    print(S)
