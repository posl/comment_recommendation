def get_input():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    return N, T, A, H

if __name__ == '__main__':
    get_input()