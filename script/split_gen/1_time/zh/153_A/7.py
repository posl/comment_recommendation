def main():
    H, A = map(int, input().split())
    print(H // A + (1 if H % A else 0))
