def get_input():
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    lr = []
    for i in range(k):
        lr.append(input().split())
    return n, k, lr

if __name__ == '__main__':
    get_input()