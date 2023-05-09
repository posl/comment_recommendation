def main():
    S = input()
    Q = int(input())
    reverse = False
    for i in range(Q):
        T = list(map(str, input().split()))
        if T[0] == '1':
            reverse = not reverse
        else:
            if T[1] == '1':
                if reverse:
                    S = S + T[2]
                else:
                    S = T[2] + S
            else:
                if reverse:
                    S = T[2] + S
                else:
                    S = S + T[2]
    if reverse:
        print(S[::-1])
    else:
        print(S)
