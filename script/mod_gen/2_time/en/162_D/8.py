def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j-i != k-j:
                    ans += 1
    print(ans)
main()
I think the solution is correct but it is too slow.
I think the solution is correct but it is too slow.
You can use itertools.combinations to generate all combinations. This will make your code much simpler.
from itertools import combinations

if __name__ == '__main__':
    main()