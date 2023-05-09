def main():
    S = input()
    Q = int(input())
    reversed = False
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            reversed = not reversed
        else:
            if query[1] == "1":
                S = query[2] + S
            else:
                S = S + query[2]
    if reversed:
        S = S[::-1]
    print(S)
