def main():
    N = int(input())
    a = list(map(int, input().split()))
    num = [0] * 200001
    ans = []
    for i in a:
        num[i] += 1
        if num[i] >= 2:
            num[i] = 0
            num[i + 1] += 1
        ans.append(sum(num))
    print(*ans, sep="
")
