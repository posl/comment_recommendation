def main():
    k = int(input())
    ans = 0
    ans_list = []
    while len(ans_list) < k:
        ans += 1
        if ans % 10 == 0:
            continue
        ans_list.append(ans)
        if ans % 10 == 2:
            ans_list.append(ans*10)
    print(ans_list[k-1])
