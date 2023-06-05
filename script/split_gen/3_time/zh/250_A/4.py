def problem250_a():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    result = 0
    if r==1 or r==h or c==1 or c==w:
        result = 2
    else:
        result = 4
    print(result)
