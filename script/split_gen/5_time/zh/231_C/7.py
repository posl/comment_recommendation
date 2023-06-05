def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for i in range(q)]
    a.sort()
    for i in range(q):
        if x[i] < a[0]:
            print(n)
        elif x[i] > a[n-1]:
            print(0)
        else:
            left = 0
            right = n-1
            while left < right:
                mid = (left+right)//2
                if a[mid] < x[i]:
                    left = mid+1
                else:
                    right = mid
            print(n-left)
