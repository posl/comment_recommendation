#Énoncé du problème
#On vous donne N chaînes de caractères S_1,S_2,...,S_N dans cet ordre.
#Imprimez S_N,S_N-1,...,S_1 dans cet ordre.
#
#Contraintes
#1≤N≤10
#N est un nombre entier.
#S_i est une chaîne de longueur comprise entre 1 et 10, inclusivement, composée de lettres anglaises minuscules, de lettres anglaises majuscules et de chiffres.
#
#Entrée
#Les donnée d’entrées sont fournies au logiciel dans le format suivant:
#N
#S_1
#S_2
#⋮
#S_N
#
#Sortie
#Imprimez N lignes. La i-ième (1≤i≤N) ligne doit contenir S_N+1-i.
#Exemple d'entrée 1
#3
#Takahashi
#Aoki
#Snuke
#
#Exemple de sortie 1
#Snuke
#Aoki
#Takahashi
#
#Exemple d'entrée 2
#4
#2023
#Year
#New
#Happy
#
#Exemple de sortie 2
#Happy
#New
#Year
#2023

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        print(S[N-1-i])

if __name__ == '__main__':
    main()