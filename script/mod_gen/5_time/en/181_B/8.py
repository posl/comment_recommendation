def main():
    n = int(input())
    total = 0
    for i in range(n):
        a,b = map(int,input().split())
        total += (b-a+1)*(a+b)/2
    print(int(total))
main()
