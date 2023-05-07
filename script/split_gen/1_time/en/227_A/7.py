def main():
    N, K, A = map(int, input().split())
    print((A + K - 1) % N + 1)
main()
import sys
input = sys.stdin.readline
