def main():
    #input
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    #output
    if H <= sum(A):
        print('Yes')
    else:
        print('No')
