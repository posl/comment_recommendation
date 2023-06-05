def main():
    a,b = map(int,input().split())
    ans = 0
    for i in range(1,20):
        if a*i>=b:
            ans = i
            break
    print(ans)
