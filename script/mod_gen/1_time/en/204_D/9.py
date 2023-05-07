def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(sum(T) - T[-1] + T[-1] // 2)
main()
I think this problem is a bit tricky. The idea is to use the two ovens as follows to cook all the dishes in 13 minutes. The first oven: Cook Dishes 5 and 1 in this order. The second oven: Cook Dishes 2, 4, and 3 in this order. The first oven is used for 5 + 1 = 6 minutes. The second oven is used for 2 + 4 + 3 = 9 minutes. The total time is 6 + 9 = 15 minutes. However, we can use the first oven for 5 + 1 + 3 = 9 minutes instead. Then, the second oven is used for 2 + 4 = 6 minutes. The total time is 9 + 6 = 15 minutes. We can reduce the total time from 15 minutes to 13 minutes by using the first oven for 3 minutes longer than the second oven.

if __name__ == '__main__':
    main()