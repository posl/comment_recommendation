def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = 1
        while a * a <= s[i]:
            if s[i] % a == 0:
                b = s[i] // a
                if a * b == s[i] and a != b:
                    if (a + b) % 2 == 1:
                        count += 1
            a += 1
    print(count)
