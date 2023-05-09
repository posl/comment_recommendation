def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            ans.append(i)
            if i != N//i:
                ans.append(N//i)
    ans.sort()
    for i in ans:
        print(i)
