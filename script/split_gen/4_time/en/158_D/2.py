def main():
    S = input()
    Q = int(input())
    S = list(S)
    reverse = False
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            reverse = not reverse
        elif (query[1] == '1') ^ reverse:
            S.insert(0, query[2])
        else:
            S.append(query[2])
    if reverse:
        S.reverse()
    print(''.join(S))
