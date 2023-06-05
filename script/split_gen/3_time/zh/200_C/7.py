def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*200
    for a in A:
        B[a%200] += 1
    count = 0
    for b in B:
        count += b*(b-1)//2
    print(count)
main()
