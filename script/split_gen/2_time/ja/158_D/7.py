def main():
    S = input()
    Q = int(input())
    S = list(S)
    flag = 0
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            if flag == 0:
                flag = 1
            else:
                flag = 0
        else:
            if query[1] == '1':
                if flag == 0:
                    S.insert(0, query[2])
                else:
                    S.append(query[2])
            else:
                if flag == 0:
                    S.append(query[2])
                else:
                    S.insert(0, query[2])
    if flag == 0:
        print(''.join(S))
    else:
        print(''.join(S[::-1]))
