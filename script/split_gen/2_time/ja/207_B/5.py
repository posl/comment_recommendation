def main():
    A, B, C, D = map(int, input().split())
    if A > B * D:
        print(-1)
        return
    if C <= B:
        print(0)
        return
    print(-(-((A - B * D) // (B * C - B * D)) + 1))
