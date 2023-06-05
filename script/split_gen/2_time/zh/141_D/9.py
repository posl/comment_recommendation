def main():
    n,k,q = map(int,input().split())
    a = [int(input()) for i in range(q)]
    score = [k]*n
    for i in range(q):
        score[a[i]-1] = score[a[i]-1] - 1
    for i in range(n):
        if score[i] > 0:
            print('Yes')
        else:
            print('No')
