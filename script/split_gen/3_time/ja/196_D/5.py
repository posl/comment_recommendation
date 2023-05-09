def main():
    H,W,A,B = map(int,input().split())
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            a = bin(i).count("1")
            b = bin(j).count("1")
            if a==A and b==B:
                ans += 1
    print(ans)
