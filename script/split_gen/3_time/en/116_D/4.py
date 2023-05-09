def main():
    N, K = map(int, input().split())
    Sushi = []
    for i in range(N):
        Sushi.append(list(map(int, input().split())))
    Sushi.sort(key=lambda x:x[1], reverse=True)
    Topping = [0]*(N+1)
    Topping[Sushi[0][0]] += 1
    ToppingNum = 1
    ToppingSum = Sushi[0][1]
    SushiEat = [Sushi[0][1]]
    for i in range(1, N):
        if Topping[Sushi[i][0]] == 0:
            Topping[Sushi[i][0]] += 1
            ToppingNum += 1
            ToppingSum += Sushi[i][1]
            SushiEat.append(Sushi[i][1])
        else:
            Topping[Sushi[i][0]] += 1
            ToppingSum += Sushi[i][1]
            SushiEat.append(Sushi[i][1])
        if ToppingNum == K:
            break
    ans = ToppingSum + ToppingNum**2
    for i in range(K, N):
        if Topping[Sushi[i][0]] == 0:
            Topping[Sushi[i][0]] += 1
            ToppingNum += 1
            ToppingSum += Sushi[i][1]
            SushiEat.append(Sushi[i][1])
            ToppingSum -= SushiEat[0]
            SushiEat.pop(0)
            while Topping[SushiEat[0]] > 1:
                ToppingSum -= SushiEat[0]
                Topping[SushiEat[0]] -= 1
                SushiEat.pop(0)
            ans = max(ans, ToppingSum + ToppingNum**2)
        else:
            Topping[Sushi[i][0]] += 1
            ToppingSum += Sushi[i][1]
            SushiEat.append(Sushi[i][1])
            ToppingSum -= SushiEat[0]
            SushiEat.pop(0)
            while Topping[SushiEat[0]] > 1:
                ToppingSum -= SushiEat[0]
                Topping[SushiEat[0]] -= 1
                SushiEat.pop(0)
            ans = max(ans, ToppingSum + T
