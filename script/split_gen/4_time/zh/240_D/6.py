def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(a)
    result = []
    for i in range(n):
        if i == 0:
            result.append(1)
            continue
        if a[i] == 2:
            result.append(result[i-1])
        else:
            result.append(result[i-1]+1)
    #print(result)
    for i in range(n):
        print(result[i])
