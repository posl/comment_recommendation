def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    gcdness = [0] * 1001
    for i in a:
        for j in range(2, i+1):
            if i % j == 0:
                gcdness[j] += 1
    print(gcdness.index(max(gcdness)))
main()
The above code is a Python 3 solution to the problem. The code is not optimized and is not intended to be used as a benchmark. The code is written for the purpose of learning and understanding the problem. The code is written by me and is original. The code is licensed under the MIT License.

if __name__ == '__main__':
    main()