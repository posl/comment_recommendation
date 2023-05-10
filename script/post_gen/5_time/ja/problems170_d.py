Synthesizing 8/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    #print(a)
    #print(len(a))
    count = 0
    for i in range(len(a)):
        #print(a[i])
        #print(i)
        #print(len(a))
        #print("i",i)
        #print("len",len(a))
        #print("a[i]",a[i])
        #print("a[i+1]",a[i+1])
        #print("a[i+2]",a[i+2])
        #print("a[i+3]",a[i+3])
        #print("a[i+4]",a[i+4])
        #print("a[i+5]",a[i+5])
        #print("a[i+6]",a[i+6])
        #print("a[i+7]",a[i+7])
        #print("a[i+8]",a[i+8])
        #print("a[i+9]",a[i+9])
        #print("a[i+10]",a[i+10])
        #print("a[i+11]",a[i+11])
        #print("a[i+12]",a[i+12])
        #print("a[i+13]",a[i+13])
        #print("a[i+14]",a[i+14])
        #print("a[i+15]",a[i+15])
        #print("a[i+16]",a[i+16])
        #print("a[i+17]",a[i+17])
        #print("a[i+18]",a[i+18])
        #print("a[i+19]",a[i+19])
        #print("a[i+20]",a[i+20])
        #print("a[i+21]",a[i+21])
        #print("a[i+22]",a[i+22])
        #print("a[i+23]",a[i+23])
        #print("a[i+24]",a[i+24])
        #print("a[i+25]",a[i+25])
        #print("a[i+26]",a[i+26])
        #print("a[i+27]",a[i+27])
        #print("a[i+28]",a[i+28])
        #print("a[i+29]",a[i+

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        else:
            if a[i] % a[i-1] != 0:
                ans += 1
    print(ans)
main()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max = a[-1]
    ans = 0
    for i in range(n):
        if a[i] == max:
            continue
        flag = True
        for j in range(i+1, n):
            if a[j] % a[i] == 0:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 5

def gcd(a,b):
    if a % b == 0:
        return(b)
    else:
        return(gcd(b,a%b))

n = int(input())
a = list(map(int,input().split()))
a.sort()
a.reverse()
l = [0]*n
r = [0]*n
l[0] = a[0]
r[n-1] = a[n-1]
for i in range(1,n):
    l[i] = gcd(l[i-1],a[i])
    r[n-1-i] = gcd(r[n-i],a[n-1-i])
ans = 1
for i in range(n):
    if i == 0:
        ans = max(ans,r[1])
    elif i == n-1:
        ans = max(ans,l[n-2])
    else:
        ans = max(ans,gcd(l[i-1],r[i+1]))
print(ans)

=======
Suggestion 6

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 7

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a
