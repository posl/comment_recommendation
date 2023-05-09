def check(a):
    if a >= sum(A) * (1 / (4 * M)):
        return True
    else:
        return False
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

if __name__ == '__main__':
    check()