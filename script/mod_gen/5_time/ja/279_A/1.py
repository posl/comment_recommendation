def solve():
    S = input()
    count = 0
    for i in range(len(S)):
        if S[i] == "v":
            count += S[i+1:].count("w")
    print(count)
solve()

if __name__ == '__main__':
    solve()