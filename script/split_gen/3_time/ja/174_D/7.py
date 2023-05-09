def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n):
        if s[i] == "R":
            count += 1
    print(min(count, n - count))
