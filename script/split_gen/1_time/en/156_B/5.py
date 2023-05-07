def main():
    n, k = map(int, input().split())
    print(len(str(n).encode("utf-8")) * 8 // math.log2(k))
