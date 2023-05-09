def main():
    n = int(input())
    w = [input() for i in range(n)]
    for i in range(n-1):
        if w[i][-1] != w[i+1][0]:
            print('No')
            return
        if w.count(w[i]) > 1:
            print('No')
            return
    print('Yes')
