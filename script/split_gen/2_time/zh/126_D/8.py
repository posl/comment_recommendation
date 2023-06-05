def main():
    n,k = map(int,input().split())
    p = 0
    for i in range(1,n+1):
        if i >= k:
            p += 1/n
        else:
            j = 1
            while i * 2 ** j < k:
                j += 1
            p += (1/2) ** j / n
    print(p)
