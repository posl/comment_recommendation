def main():
    N = int(input())
    ans = 0
    for i in range(1, 10**6):
        if i**3 > N:
            break
        for j in range(i+1, 10**6):
            if i*j**3 > N:
                break
            ans += 1
    print(ans)
