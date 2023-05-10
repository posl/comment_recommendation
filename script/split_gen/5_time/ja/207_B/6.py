def main():
    A,B,C,D = map(int,input().split())
    if B >= C*D:
        print(-1)
    else:
        count = 0
        while A > 0:
            A -= B
            count += 1
            A += C
        print(count)
