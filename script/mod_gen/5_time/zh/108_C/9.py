def abc(n,k):
    ans = 0
    for a in range(1,n+1):
        for b in range(1,n+1):
            for c in range(1,n+1):
                if (a+b)%k == 0 and (b+c)%k == 0 and (c+a)%k == 0:
                    ans += 1
    return ans

if __name__ == '__main__':
    abc()