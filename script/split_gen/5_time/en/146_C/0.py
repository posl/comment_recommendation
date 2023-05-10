def main():
    A, B, X = map(int, input().split())
    ans = 0
    if A * 10 ** 9 + B * 10 <= X:
        ans = 10 ** 9
    else:
        for i in range(1, 10):
            if A * i ** 9 + B * len(str(i)) <= X:
                ans = i
    print(ans)
