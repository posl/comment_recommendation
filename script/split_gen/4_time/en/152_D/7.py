def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if i%10 == 0:
            continue
        else:
            last = int(str(i)[-1])
            first = int(str(i)[0])
            if last == first:
                ans += 1
    print(ans)
