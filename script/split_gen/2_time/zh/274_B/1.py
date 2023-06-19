def get_input():
    h,w = map(int,input().split())
    x = []
    for i in range(h):
        x.append(list(input()))
    return h,w,x
