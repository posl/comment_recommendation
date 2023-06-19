def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = 1
        b = 1
        while 4*a*b+3*a+3*b<s[i]:
            if a==b:
                b+=1
            else:
                a+=1
        if 4*a*b+3*a+3*b!=s[i]:
            count+=1
    print(count)
