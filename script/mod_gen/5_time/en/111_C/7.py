def main():
    n = int(input())
    v = list(map(int, input().split()))
    v_even = v[0::2]
    v_odd = v[1::2]
    v_even.sort()
    v_odd.sort()
    v_even_max = max(v_even, key=v_even.count)
    v_odd_max = max(v_odd, key=v_odd.count)
    if v_even_max != v_odd_max:
        print(n - v_even.count(v_even_max) - v_odd.count(v_odd_max))
    else:
        if v_even.count(v_even_max) > v_odd.count(v_odd_max):
            print(n - v_even.count(v_even_max) - v_odd.count(v_odd_max))
        else:
            print(n - v_even.count(v_even_max) - v_odd.count(v_odd_max) + 1)
main()

if __name__ == '__main__':
    main()