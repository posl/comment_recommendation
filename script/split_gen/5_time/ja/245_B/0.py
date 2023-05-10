def main():
    n = int(input())
    a = set(map(int, input().split()))
    for i in range(2000):
        if i not in a:
            print(i)
            exit()
