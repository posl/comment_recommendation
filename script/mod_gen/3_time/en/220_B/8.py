def base_k_to_10(num, k):
    num = str(num)
    return sum([int(i) * (k ** j) for j, i in enumerate(num[::-1])])
k = int(input())
a, b = input().split()
print(base_k_to_10(a, k) * base_k_to_10(b, k))

if __name__ == '__main__':
    base_k_to_10()