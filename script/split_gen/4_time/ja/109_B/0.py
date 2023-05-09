def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(n-1):
        if w[i][-1] != w[i+1][0]:
            print('No')
            return
    if len(set(w)) != n:
        print('No')
        return
    print('Yes')
    return
