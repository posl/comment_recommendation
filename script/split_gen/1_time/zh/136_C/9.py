def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n - 1):
        if h[i] > h[i + 1]:
            h[i] -= 1
        elif h[i] == h[i + 1]:
            pass
        else:
            print('No')
            break
    else:
        print('Yes')
