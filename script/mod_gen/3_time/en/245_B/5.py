def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[n-1] == 2000:
        print(0)
    else:
        for i in range(n):
            if a[i] != i:
                print(i)
                break
main()
The main idea is to sort the list and then check if the largest element is 2000. If it is, then the answer is 0. Otherwise, we check from the smallest element to the largest element, and if the element is not equal to its index, then the answer is the index.
The time complexity is O(nlogn) and the space complexity is O(n).
Problem 246

if __name__ == '__main__':
    main()