import random
import math
import time
import datetime
import pdb
import binascii


#TODO
#   1. Do a binary search oN the primeList for more efficiency, lower runtime || doNe 
#   2. Fix the most retarded algorithm every invented ||  working oN that
#   3. Fix a case for greater than in binaryAlgorithm || doNe
#   4. Determine scenario where x not in z, return False
#   5. Fix binary algo, i need to get 2 general while cases.
#      while between 0 and 50 is true, half middle and stay in that 0 | 50 range
#      Other way around while between 50 and 100,
#      increase  the middle and stay in that 50 | 100 rang
#   6. binaryAlgorithm needs a False case || DONE
#   7. Magic number calculation doesn't work, figure it out || you could give random magic numbers
#       Until one works, if it works, the number returned will be d! and the number used e!



#Global primeList, stores prime numbers
primeList = []
testList = []
#   --> Create a dummy list to envoke binary searches oN
for c in range(1, 1000):
    testList.append(c)

#   --> Recursive binary search.
#       Using recursioN, you exclude the other half oN every functioN call.
#       z: list | x: value to find | lv: 0 left value | rv: list inversed [-1] | lastValue: 0
#       Return True if x occurs in z
def binaryAlgorithm(z, x, lv, rv, lastValue):
    mid = int((lv + rv) // 2)
    #If lastValue, which is the mid value from the previous recursioN
    #is equal to the mid value calculated from the current recursioN 
    #return False, because we're now stuck in dead search space
    if lastValue == mid:
        return False

    #Value found, return True
    if z[mid] == x:
        return True

    #Discard the right side of the search space
    elif x < z[mid]:
        print(mid, "|| Searching...")
        return binaryAlgorithm(z, x, lv, mid, mid)

    #Discard the left side of the search space
    elif x > z[mid]:
        print(mid, "|| Searching...")
        return binaryAlgorithm(z, x, mid, rv, mid)


#   --> Return true if x is a prime,
#       Return false if x is not a prime OR if it already exists in z
def isPrime(x):
    #DoN't bother iterating if x is already in primeList
    try:
        if(binaryAlgorithm(primeList, x, 0, len(primeList), x) == True):
            return False
    except IndexError as e: #Out of bounds, the list begins empty
        pass

    if x == 0 or x == 1:
        return False
    if x == 2 or x == 3:
        return True

    else:
        #If x module num is possible, then there is another common
        #Divider among x, making it not a prime number
        for num in range(2, x):
            if x % num == 0:
                return False

    print("Prime Found")
    return True

#   --> Find the relative primes for e and d, using the two large prime numbers
#       Returns a list of (most) relative numbers, some don't work!, test these by finding
#       if they rule out 1 with dCheck
def findCoPrime(p, q):
    #pubKey = [x,n]
    n = p * q
    oN = ((p - 1) * (q - 1))
    magicNumbers = []

    #Fix this retarded structure asap please
    for e in range (2, oN):
        isFalse = []
        result = e / n
        if result.is_integer() == True:
            isFalse.append(False)
        else:
            isFalse.append(True)

        result = e / p
        if result.is_integer() == True:
            isFalse.append(False)
        else:
            isFalse.append(True)

        result = e / q
        if result.is_integer() == True:
            isFalse.append(False)
        else:
            isFalse.append(True)

        result = oN / e
        if result.is_integer() == True:
            isFalse.append(False)
        else:
            isFalse.append(True)

        if isFalse[0] == True and isFalse[1] == True and isFalse[2] == True and isFalse[3] == True:
            magicNumbers.append(e)
            #print(e)

    return magicNumbers


#   --> Returns d if found
#       D can be any number from the magicNumbers list, test some out.
#       If dCheck returns a number from that magicNumbers list, you can use it for decryption
#       oN is a fixed value calculated from (p - 1) (p - 1)
#       e is any a magic number, find one that rules out 1!
def dCheck(e, oN):

    i = 1
    while True:
        if((i * e) % oN == 1): #Check if e can be used for d too
            print(i)
            return i
        i += 1
        print((i * e) % oN, " || ", i)



def main():

    lastTime = datetime.datetime.now() #Keep track of time to meassure time between primes
    for c in testList: #Iterate i times, trying to find primes i times in the range of x
        x = int(random.random() * 101)
        if isPrime(x) == True:
            print(datetime.datetime.now() - lastTime, " || " ,len(primeList))
            lastTime = datetime.datetime.now()
            primeList.append(x)
            primeList.sort()
    print(primeList, "\n")



    x = findCoPrime(41,61) #p and q
    print(x)
    p = dCheck(23,2400)
    print(p)



    #x = "guerangioer323"
    #x = binascii.hexlify(x.encode())
    #print(x)









main()
