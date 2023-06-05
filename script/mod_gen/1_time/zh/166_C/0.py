def get_input():
    n,m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]
    return n,m,h,ab

if __name__ == '__main__':
    get_input()