def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    a.sort(reverse=True)
    b.sort(reverse=True)
    a_sum = sum(a)
    b_sum = 0
    num = 0
    for i in range(n):
        a_sum -= a[i]
        b_sum += a[i] + b[i]
        num += 1
        if b_sum > a_sum:
            break
    print(num)
main()
#解答
#在每个镇上发表演讲的候选人都会获得该镇的所有选票。
#因此，高桥至少需要在具有最多支持高桥的选民的镇上发表演讲。
#因此，我们首先按照支持高桥的选民的数量对镇进行排序。
#然后，我们按照这个顺序依次发表演讲。
#在这种情况下，高桥将获得最多的选票。
#我们将在高桥获得的选票数超过青木获得的选票数时停止发表演讲。

if __name__ == '__main__':
    main()