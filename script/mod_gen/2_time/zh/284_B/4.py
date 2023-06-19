def get_input():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        yield (N, A)

if __name__ == '__main__':
    get_input()