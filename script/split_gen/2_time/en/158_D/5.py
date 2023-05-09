def main():
    S = list(input())
    Q = int(input())
    reverse = 0
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            reverse += 1
        else:
            if (int(query[1]) + reverse) % 2 == 0:
                S.append(query[2])
            else:
                S.insert(0, query[2])
    if reverse % 2 == 1:
        S = S[::-1]
    print(''.join(S))
