def get_input():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    return N, A

if __name__ == '__main__':
    get_input()