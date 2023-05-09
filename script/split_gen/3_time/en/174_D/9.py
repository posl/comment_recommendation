def main():
    count = 0
    n = int(input())
    c = input()
    for i in range(n):
        if c[i] == 'W':
            count += 1
    print(count - (count // 2))
