def main():
    N = int(input())
    for i in range(N):
        a, s = map(int, input().split())
        if s < a:
            print('No')
        else:
            if (s - a) % 2 == 0:
                print('Yes')
            else:
                print('No')
