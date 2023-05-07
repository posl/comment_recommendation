def main():
    A, B = map(int, input().split())
    ans = -1
    for i in range(1000):
        if A == i*8//100 and B == i*10//100:
            ans = i
            break
    print(ans)
