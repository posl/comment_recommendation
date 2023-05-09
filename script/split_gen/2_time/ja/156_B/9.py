def main():
    N, K = map(int, input().split())
    print(len(str(N)))
    print(len(str(N).replace("0", "")))
    print(len(str(N).replace("0", "")) + 1)
