def main():
    S = input()
    Q = int(input())
    query = [list(map(str, input().split())) for _ in range(Q)]
    flag = 0
    for q in query:
        if q[0] == "1":
            flag = 1 - flag
        else:
            if (q[1] == "1" and flag == 0) or (q[1] == "2" and flag == 1):
                S = q[2] + S
            else:
                S = S + q[2]
    if flag == 1:
        S = S[::-1]
    print(S)
