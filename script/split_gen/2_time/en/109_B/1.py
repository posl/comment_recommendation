def main():
    n = int(input())
    words = [input() for _ in range(n)]
    if len(set(words)) != n:
        print('No')
        return
    for i in range(1, n):
        if words[i][0] != words[i-1][-1]:
            print('No')
            return
    print('Yes')
