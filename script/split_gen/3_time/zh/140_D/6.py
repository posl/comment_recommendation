def main():
    n,k = map(int,input().split())
    s = input()
    #print(n,k,s)
    count = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
    count = min(count+2*k,n-1)
    print(count)
