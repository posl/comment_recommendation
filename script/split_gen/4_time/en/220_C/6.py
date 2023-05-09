def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    x = int(input())
    a_sum = sum(a_list)
    a_len = len(a_list)
    b_len = (x // a_sum) * a_len
    b_sum = (x // a_sum) * a_sum
    for a in a_list:
        b_len += 1
        b_sum += a
        if b_sum > x:
            break
    print(b_len)
