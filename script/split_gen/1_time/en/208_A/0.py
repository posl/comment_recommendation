def main():
    a, b = map(int, input().split())
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == b and a == 2:
                print('Yes')
                return
    print('No')
