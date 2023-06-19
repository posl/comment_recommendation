def main():
    N = int(input())
    a = [0] * (N-1)
    b = [0] * (N-1)
    for i in range(N-1):
        a[i], b[i] = map(int, input().split())
    #print(a)
    #print(b)
    flag = False
    for i in range(N-1):
        if a[i] == 1 or b[i] == 1:
            flag = True
            break
    if flag:
        print('Yes')
    else:
        print('No')
