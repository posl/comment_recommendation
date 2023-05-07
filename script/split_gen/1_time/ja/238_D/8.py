def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        ans = "No"
        if a <= s:
            if (s - a) % 2 == 0:
                ans = "Yes"
        print(ans)
