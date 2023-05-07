def main():
    N = int(input())
    print(len(set(tuple(map(int, input().split()))[1:] for _ in range(N))))
