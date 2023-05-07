def main():
    #Get input from user
    n, k = input().split()
    n = int(n)
    k = int(k)
    a = input().split()
    a = [int(i) for i in a]
    
    #Initialize variables
    takahashi = 0
    aoki = 0
    i = 0
    while i < k:
        if a[i] > n:
            break
        else:
            takahashi += a[i]
            n -= a[i]
            i += 1
    takahashi += n
    print(takahashi)
