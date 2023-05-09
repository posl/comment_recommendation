def main():
    S = input()
    Q = int(input())
    is_reverse = False
    for _ in range(Q):
        query = input().split()
        if len(query) == 1:
            is_reverse = not is_reverse
        else:
            if query[1] == '1':
                if is_reverse:
                    S = S + query[2]
                else:
                    S = query[2] + S
            else:
                if is_reverse:
                    S = query[2] + S
                else:
                    S = S + query[2]
    if is_reverse:
        print(S[::-1])
    else:
        print(S)
