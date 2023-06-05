def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    a = set(a)
    if len(a) == n:
        print('Yes')
    else:
        print('No')
