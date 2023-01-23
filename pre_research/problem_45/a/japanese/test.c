//上底の長さが a、下底の長さが b、高さが h の台形があります。
//この台形の面積を求めてください。
//1≤a≤100
//1≤b≤100
//1≤h≤100
//入力で与えられる値はすべて整数
//h は偶数
//入力例1
//3
//4
//2
//出力例1
//7

#include <stdio.h>
int main(void){
    int a,b,h;
    scanf("%d",&a);
    scanf("%d",&b);
    scanf("%d",&h);
    printf("%d",(a+b)*h/2);
    return 0;
}
