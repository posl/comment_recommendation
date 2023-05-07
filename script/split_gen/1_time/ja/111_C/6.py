def main():
    n = int(input())
    v = list(map(int, input().split()))
    v_odd = v[::2]
    v_even = v[1::2]
    v_odd_count = max(v_odd.count(x) for x in set(v_odd))
    v_even_count = max(v_even.count(x) for x in set(v_even))
    ans = min(n - v_odd_count, n - v_even_count)
    if len(set(v_odd)) == len(set(v_even)) == 1 and v_odd[0] != v_even[0]:
        ans = min(ans, n // 2)
    print(ans)
