def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        for j in range(t+1):
            s = s.replace('a', 'bc')
            s = s.replace('b', 'ca')
            s = s.replace('c', 'ab')
        print(s[k-1])
