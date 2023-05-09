def main():
    K = int(input())
    #K = 923423423420220108
    #K = 11
    #K = 3
    ans = ""
    while K > 0:
        ans = str(K % 2) + ans
        K //= 2
    print(ans)
