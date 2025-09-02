T = int(input("Number of tests?"))
for i in range(T):
    S = input("Give me the word: ")
    print(S[::2]," ", S[1::2])
