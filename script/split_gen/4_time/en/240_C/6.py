def main():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        a_,b_ = map(int,input().split())
        a.append(a_)
        b.append(b_)
    distance = 0
    for i in range(N):
        distance += a[i]
        if distance > X:
            print('No')
            return
        distance += b[i]
    if distance > X:
        print('No')
        return
    print('Yes')
    return
