def main():
    K = int(input())
    ans = []
    i = 1
    while len(ans) < K:
        sum = 0
        for j in str(i):
            sum += int(j)
        if i / sum >= (i + 1) / (sum + 1):
            ans.append(i)
        i += 1
    for i in ans:
        print(i)
