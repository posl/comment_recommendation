def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    result = []
    for i in range(n):
        if i == 0:
            result.append(t[0])
        else:
            if t[i] < result[i-1]:
                result.append(t[i])
            else:
                result.append(t[i]+s[i])
    for i in result:
        print(i)
