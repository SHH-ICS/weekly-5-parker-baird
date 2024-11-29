word = (input())
if word.isdigit():
    word = int(word)
    if word < 0:
        print("This program does not input symbols, letters, decimals, or negative integers try again.")
    i = 0
    j = 1
    for n in range(word+1):
        i += j*((4/(2*n+1)))
        j *= -1
    print(i)
else:
    print("This program does not input symbols, letters, decimals, or negative integers try again.")