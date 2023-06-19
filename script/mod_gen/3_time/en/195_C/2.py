def main():
    N = int(input())
    print(N - N//(10**3) - N//(10**6) - N//(10**9) - N//(10**12) - N//(10**15))
main()
