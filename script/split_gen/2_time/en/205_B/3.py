def main():
    n = int(input())
    a = input().split()
    a = [int(i) for i in a]
    a.sort()
    if a == list(range(1,n+1)):
        print('Yes')
    else:
        print('No')
