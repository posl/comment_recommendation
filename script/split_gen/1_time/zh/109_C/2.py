def main():
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    x_list.append(x)
    x_list.sort()
    x_list = [x_list[i+1]-x_list[i] for i in range(n)]
    import math
    def gcd(a,b):
        if b == 0:
            return a
        else:
            return gcd(b,a%b)
    answer = x_list[0]
    for i in range(1,n):
        answer = gcd(answer,x_list[i])
    print(answer)
