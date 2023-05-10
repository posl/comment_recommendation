def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    return N, A, B, C

if __name__ == '__main__':
    get_input()