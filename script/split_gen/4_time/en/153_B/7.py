def main():
    H,N = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    if H <= sum(A):
        print('Yes')
    else:
        print('No')