def main():
    V, T, S, D = map(int, input().split())
    print('No') if T * V <= D <= S * V else print('Yes')
