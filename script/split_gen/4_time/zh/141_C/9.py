def main():
    n,k,q = map(int,input().split())
    player = [0]*n
    for i in range(q):
        player[int(input())-1] += 1
    for i in range(n):
        if k - q + player[i] > 0:
            print('Yes')
        else:
            print('No')
