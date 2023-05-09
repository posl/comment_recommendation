def main():
    S = input()
    Q = int(input())
    reverse = False
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            reverse = not reverse
        else:
            if reverse:
                if query[1] == '1':
                    S += query[2]
                else:
                    S = query[2] + S
            else:
                if query[1] == '1':
                    S = query[2] + S
                else:
                    S += query[2]
    if reverse:
        S = S[::-1]
    print(S)
