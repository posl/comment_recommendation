def get_inputs():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    return N, xy

if __name__ == '__main__':
    get_inputs()