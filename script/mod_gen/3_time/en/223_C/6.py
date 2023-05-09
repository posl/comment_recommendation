def get_input():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        line = input()
        A.append(int(line.split()[0]))
        B.append(int(line.split()[1]))
    return N, A, B

if __name__ == '__main__':
    get_input()