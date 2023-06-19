def main():
    N = input()
    A = input()
    print(1/sum([1/int(i) for i in A.split()]))
main()
