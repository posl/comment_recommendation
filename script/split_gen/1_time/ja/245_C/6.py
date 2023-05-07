def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    #print(a)
    #print(b)
    def check(x):
        #print("x=",x)
        cnt = 0
        for i in range(n):
            if a[i] <= x:
                cnt += 1
        #print("cnt=",cnt)
        if cnt == n:
            return True
        cnt = 0
        for i in range(n):
            if b[i] <= x:
                cnt += 1
        #print("cnt=",cnt)
        if cnt == n:
            return True
        cnt = 0
        for i in range(n):
            if a[i] <= x and b[i] <= x:
                cnt += 1
        #print("cnt=",cnt)
        if cnt == n:
            return True
        cnt = 0
        for i in range(n-1):
            if a[i] <= x and a[i+1] <= x:
                cnt += 1
        #print("cnt=",cnt)
        if cnt == n-1:
            return True
        cnt = 0
        for i in range(n-1):
            if b[i] <= x and b[i+1] <= x:
                cnt += 1
        #print("cnt=",cnt)
        if cnt == n-1:
            return True
        cnt = 0
        for i in range(n-1):
            if a[i] <= x and b[i+1] <= x:
                cnt += 1
        #print("cnt=",cnt)
        if cnt == n-1:
            return True
        cnt = 0
        for i in range(n-1):
            if b[i] <= x and a[i+1] <= x:
                cnt += 1
        #print("cnt=",cnt)
        if cnt == n-1:
            return True
        return False
    #print(check(1))
    #print(check(2))
    #print(check(3))
    #print(check(4))
    #print(check(5))
    #print(check(6))
    #print(check(7))
    #print(check(8))
    #print(check(
