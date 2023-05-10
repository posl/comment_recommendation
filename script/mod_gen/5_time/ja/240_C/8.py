def check(N,X,ab):
    pos = 0
    for i in range(N):
        pos += ab[i][1]
        if pos > X:
            return False
        pos -= ab[i][0]
        if pos < 0:
            return False
    return True
N,X = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(N)]
print('Yes' if check(N,X,ab) else 'No')

if __name__ == '__main__':
    check()