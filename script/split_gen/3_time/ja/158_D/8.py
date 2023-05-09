def main():
    S = input()
    Q = int(input())
    N = len(S)
    rev = 0
    for i in range(Q):
        query = list(map(str, input().split()))
        if len(query) == 1:
            rev += 1
        else:
            if query[1] == '1':
                if rev % 2 == 0:
                    S = query[2] + S
                else:
                    S = S + query[2]
            else:
                if rev % 2 == 0:
                    S = S + query[2]
                else:
                    S = query[2] + S
    if rev % 2 == 1:
        S = S[::-1]
    print(S)
