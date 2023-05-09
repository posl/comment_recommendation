def main():
    N = int(input())
    # お菓子が0個の場合は0通り
    if N == 0:
        print(0)
    else:
        # お菓子が1個以上の場合は、N個のうち1個以上を取る方法がN通りある
        print(N)

if __name__ == '__main__':
    main()