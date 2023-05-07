def main():
    #input
    n = int(input())
    #compute
    if n % 111 == 0:
        ans = n
    else:
        ans = int((n / 111 + 1) * 111)
    #output
    print(ans)
