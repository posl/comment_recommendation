def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a[::-1]
    ans = 0
    for i in range(n-1):
        if a[i] <= a[i+1]:
            continue
        else:
            ans += a[i] - a[i+1]
            a[i+1] = a[i]
    print(ans)
main()
The first line of the input is the number of persons N. The second line is the heights of the persons A_1, A_2, ..., A_N. We want to have each person stand on a stool of some heights - at least zero - so that the following condition is satisfied for every person:
Condition: Nobody in front of the person is taller than the person. Here, the height of a person includes the stool.
Find the minimum total height of the stools needed to meet this goal.
We can see that the problem is equivalent to the following. For each person, we want to have the person stand on a stool of height at least the height of the tallest person in front of the person. So, we want to have the person stand on a stool of height at least the maximum height of the persons in front of the person. We can see that the answer is the sum of the differences between the heights of the persons and the heights of the stools.
So, we can solve the problem by going through the persons in reverse order. When we want to have the i-th person stand on a stool of height at least a_i, we can see that the i-th person can stand on a stool of height at least a_i if and only if the i-th person is taller than the i+1-th person. If the i-th person is not taller than the i+1-th person, we can see that the i-th person can stand on a stool of height at least a_i if and only if the i+1-th person stands on a stool of height at least a_i - (a_i - a_{i+1}). So, we can see that we can make the i-th person stand on a stool of height at least a_i if and only if the i+1-th person stands on a stool of height at least a_i. If the i-th person is taller than the i+1-th person, we can see that the i-th person can stand on a stool of height at least a_i

if __name__ == '__main__':
    main()