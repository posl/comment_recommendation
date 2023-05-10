def main():
    N = int(input())
    count = 0
    for i in range(3, len(str(N))+1):
        for j in ['7', '5', '3']:
            for k in itertools.product(['7', '5', '3'], repeat=i):
                if int(''.join(k)) <= N and j in k and len(set(k)) == 3:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()