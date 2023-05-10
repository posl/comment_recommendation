def get_input():
    h,w,n = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(n)]
    return h,w,n,ab
