def main():
    x,k,d = map(int,input().split())
    x = abs(x)
    num = x//d
    if k <= num:
        ans = x - k * d
    else:
        if (k - num) % 2 == 0:
            ans = x - num * d
        else:
            ans = abs(x - (num+1) * d)
    print(ans)
