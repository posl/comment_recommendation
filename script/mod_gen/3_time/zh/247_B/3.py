def get_input():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    return N, names

if __name__ == '__main__':
    get_input()