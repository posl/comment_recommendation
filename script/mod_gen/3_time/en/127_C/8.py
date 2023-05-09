def main():
    N, M = map(int, input().split())
    gates = [tuple(map(int, input().split())) for _ in range(M)]
    gates.sort(key=lambda x: x[1])
    ans = 0
    end = 0
    for gate in gates:
        if gate[0] > end:
            end = gate[1]
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()