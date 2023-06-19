def main():
    s=input()
    n=len(s)
    ans=10**9
    for i in range(n-2):
        x=int(s[i:i+3])
        ans=min(ans,abs(x-753))
    print(ans)
