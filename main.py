squere_one = int(input())
squere_two = int(input())

if squere_one<=squere_two :
    print("Wrong order!")
elif (squere_one-squere_two)%2==1 :
    print("Wrong difference!")
else :
    x=0
    while x<((squere_one-squere_two)/2) :
        k=0
        while k<squere_one :
            print("* ",end="")
            k += 1
        print("")
        x += 1
    z = (squere_one-squere_two)/2
    while z < (squere_one+squere_two)/2 :
        k=0
        while k<(squere_one-squere_two)/2 :
            print("* ",end="")
            k += 1
        k=0
        while k<squere_two :
            print("  ",end="")
            k += 1
        k=0
        while k<(squere_one-squere_two)/2 :
            print("* ",end="")
            k += 1
        print("")
        z += 1
        x = ((squere_one + squere_two) / 2)
    while x < squere_one :
        k = 0
        while k < squere_one:
            print("* ", end="")
            k += 1
        print("")
        x += 1