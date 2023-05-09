def main():
    S = input()
    Q = int(input())
    reverse = False
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            reverse = not reverse
        else:
            if query[1] == "1":
                if reverse:
                    S = S + query[2]
                else:
                    S = query[2] + S
            else:
                if reverse:
                    S = query[2] + S
                else:
                    S = S + query[2]
    if reverse:
        print(S[::-1])
    else:
        print(S)
