def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a > s:
            print('No')
        elif (s - a) % 2 == 1:
            print('No')
        else:
            print('Yes')
