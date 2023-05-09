def main():
    N = int(input())
    ans = []
    for i in range(2**15):
        if (i & N) == i:
            ans.append(i)
    for i in ans:
        print(i)
