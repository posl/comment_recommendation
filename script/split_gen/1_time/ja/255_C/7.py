def main():
    x,a,d,n = map(int,input().split())
    ans = 0
    if d == 0:
        ans = abs(x-a)
    else:
        if x == a:
            ans = 0
        else:
            if d > 0:
                if x < a:
                    ans = abs(x-a)
                else:
                    if (x-a)%d == 0:
                        ans = 0
                    else:
                        ans = min(abs(x-a)%d,abs(x-a)%d-d)
            else:
                if x > a:
                    ans = abs(x-a)
                else:
                    if (x-a)%d == 0:
                        ans = 0
                    else:
                        ans = min(abs(x-a)%d,abs(x-a)%d-d)
    print(ans)
