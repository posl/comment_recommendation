def solve():
    # Implement solution here
    a,b,c = map(int,input().split())
    print(a+b+c-max(a,b,c))
