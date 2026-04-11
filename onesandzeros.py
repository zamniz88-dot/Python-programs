def numberOfBits(n):
    ones = 0
    zero =0

    while (n):

        if(n&1==1):
            ones+=1
        else:
            zeros+=1

        n >>= 1
    print("\n\nOnes = ",ones,"\nZeros")

number = int(input("Enter your number : "))
numberOfBits(number)