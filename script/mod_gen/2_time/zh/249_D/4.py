def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    #print(A)
    # 1. A[i] / A[j] = A[k]
    # 2. A[i] / A[k] = A[j]
    # 3. A[j] / A[i] = A[k]
    # 4. A[j] / A[k] = A[i]
    # 5. A[k] / A[i] = A[j]
    # 6. A[k] / A[j] = A[i]
    # 1. A[i] = A[k] * A[j]
    # 2. A[i] = A[j] / A[k]
    # 3. A[j] = A[i] * A[k]
    # 4. A[j] = A[k] / A[i]
    # 5. A[k] = A[i] * A[j]
    # 6. A[k] = A[j] / A[i]
    # 1. A[i] * A[j] = A[k]
    # 2. A[i] / A[j] = A[k]
    # 3. A[j] * A[k] = A[i]
    # 4. A[j] / A[k] = A[i]
    # 5. A[k] * A[i] = A[j]
    # 6. A[k] / A[i] = A[j]
    # 1. A[i] = A[k] - A[j]
    # 2. A[i] = A[j] / A[k]
    # 3. A[j] = A[i] * A[k]
    # 4. A[j] = A[k] / A[i]
    # 5. A[k] = A[i] + A[j]
    # 6. A[k] = A[j] - A[i]
    # 1. A[i] = A[k] * A[j]
    # 2. A[i] = A[j] / A[k]
    # 3. A[j] = A[i] * A[k]
    # 4. A[j] = A[k] / A[i]
    # 5. A[k] = A[i] + A[j]
    #

if __name__ == '__main__':
    main()