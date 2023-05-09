def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [a % M for a in A]
    A = [a - M for a in A if a - M > 0] + A
    A = [a + M for a in A if a + M < 0] + A
    A.sort()
    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()
    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()
    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()
    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()
    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()
    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()
    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()
    A = [a + M for a in A if a + M < 0] + A
    A = [a - M for a in A if a - M > 0] + A
    A.sort()
    A = [a + M for a in A if a + M < 0] + A
    A = [a
