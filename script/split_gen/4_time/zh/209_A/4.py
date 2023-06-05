def problem209_a():
    a,b = map(int,input().split())
    print(b-a+1 if a<=b else 0)
