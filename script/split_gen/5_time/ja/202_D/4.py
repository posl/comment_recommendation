def main():
    a, b, k = map(int, input().split())
    ans = []
    for i in range(a):
        ans.append('a')
    for i in range(b):
        ans.append('b')
    ans.sort()
    ans = [''.join(ans)]
    for i in range(k-1):
        ans.append(next_permutation(ans[-1]))
    print(ans[-1])
