def main():
    #input
    L, R = map(int, input().split())
    #compute
    if R - L >= 2019:
        ans = 0
    else:
        ans = 2018
        for i in range(L, R):
            for j in range(i+1, R+1):
                if (i*j) % 2019 < ans:
                    ans = (i*j) % 2019
    #output
    print(ans)
