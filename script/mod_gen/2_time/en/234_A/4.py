def main():
    t = int(input())
    f = lambda x: x * x + 2 * x + 3
    print(f(f(f(t)+t)+f(f(t))))
main()
