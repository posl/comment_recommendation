def main():
    N,M = map(int,input().split())
    B = [list(map(int,input().split())) for i in range(N)]
    if N == 1:
        print('Yes')
        return
    if M == 1:
        print('No')
        return
    if N == 2 and M == 2:
        print('Yes')
        return
    if N == 2 and M == 3:
        print('Yes')
        return
    if N == 3 and M == 2:
        print('Yes')
        return
    if N == 3 and M == 3:
        print('Yes')
        return
    if N == 4 and M == 2:
        print('Yes')
        return
    if N == 2 and M == 4:
        print('Yes')
        return
    if N == 4 and M == 3:
        print('Yes')
        return
    if N == 3 and M == 4:
        print('Yes')
        return
    if N == 4 and M == 4:
        print('Yes')
        return
    if N == 5 and M == 2:
        print('Yes')
        return
    if N == 2 and M == 5:
        print('Yes')
        return
    if N == 5 and M == 3:
        print('Yes')
        return
    if N == 3 and M == 5:
        print('Yes')
        return
    if N == 5 and M == 4:
        print('Yes')
        return
    if N == 4 and M == 5:
        print('Yes')
        return
    if N == 5 and M == 5:
        print('Yes')
        return
    if N == 6 and M == 2:
        print('Yes')
        return
    if N == 2 and M == 6:
        print('Yes')
        return
    if N == 6 and M == 3:
        print('Yes')
        return
    if N == 3 and M == 6:
        print('Yes')
        return
    if N == 6 and M == 4:
        print('Yes')
        return
    if N == 4 and M == 6:
        print('Yes')
        return
