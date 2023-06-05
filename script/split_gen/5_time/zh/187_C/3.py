def main():
    N = int(input())
    s = [input() for i in range(N)]
    s = set(s)
    ans = "satisfiable"
    for i in s:
        if "!" + i in s:
            ans = i
            break
    print(ans)
