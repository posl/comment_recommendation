def get_input():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, D, A

if __name__ == '__main__':
    get_input()