def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    #print(a)
    ans = 0
    for i in range(n):
        if i == 0:
            if a[i] != a[i+1]:
                ans += 1
        elif i == n-1:
            if a[i] != a[i-1]:
                ans += 1
        else:
            if a[i] != a[i+1] and a[i] != a[i-1]:
                ans += 1
    print(ans)
main()
I solved this problem by using the sorted function to sort the array, and then I just had to check if the elements of the array were equal to the element before and after them. If they weren’t, then I added 1 to the answer. I got a score of 100.

if __name__ == '__main__':
    main()