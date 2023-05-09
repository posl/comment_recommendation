def main():
    n,k,q = map(int,input().split())
    point = [k] * n
    for i in range(q):
        a = int(input())
        point[a-1] += 1
    for j in range(n):
        if point[j] - q <= 0:
            print('No')
        else:
            print('Yes')
