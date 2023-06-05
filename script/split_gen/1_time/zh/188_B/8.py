def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    if sum([a[i]*b[i] for i in range(n)]) == 0:
        print('Yes')
    else:
        print('No')
