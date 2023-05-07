def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        T = list(map(str, input().split()))
        if T[0] == '1':
            S = S[::-1]
        elif T[0] == '2':
            if T[1] == '1':
                S = T[2] + S
            elif T[1] == '2':
                S = S + T[2]
    print(S)
