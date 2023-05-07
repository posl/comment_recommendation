def main():
    N = int(input())
    for i in range(N):
        print(*[1]+[n for n in range(1,i+1) if n!=i]+[1])
main()
