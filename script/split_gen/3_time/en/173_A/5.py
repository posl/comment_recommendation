def main():
    #input
    N = int(input())
    #calculate
    ans = 1000 - N % 1000
    if ans == 1000:
        ans = 0
    #output
    print(ans)
