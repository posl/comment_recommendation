def main():
    n = int(input())
    w = [input() for _ in range(n)]
    if len(w) != len(set(w)):
        print('No')
        return
    for i in range(1, n):
        if w[i][0] != w[i-1][-1]:
            print('No')
            return
    print('Yes')
