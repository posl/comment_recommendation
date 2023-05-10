def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        #print("i", i)
        for j in range(1, i+1):
            #print("j", j)
            if i % j == 0:
                ans += i
    print(ans)
