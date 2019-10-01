import random
import math
import time
import datetime
import pdb
import binascii


#TODO
#   1. Do a binary search oN the primeList for more efficiency, lower runtime || doNe 
#   2. Fix the most retarded algorithm every invented ||  Done
#   3. Fix a case for greater than in binaryAlgorithm || doNe
#   4. Determine scenario where x not in z, return False || Done
#   5. Fix binary algo, i need to get 2 general while cases.
#      while between 0 and 50 is true, half middle and stay in that 0 | 50 range
#      Other way around while between 50 and 100,
#      increase  the middle and stay in that 50 | 100 rang || Done
#   6. binaryAlgorithm needs a False case || DONE
#   7. Magic number calculation doesn't work, figure it out || you could give random magic numbers
#       Until one works, if it works, the number returned will be d! and the number used e! || DONE


#   --> Find the relative primes for e, test a random relative prime for d, with dCheck
#       p & q are prime numbers, returns n, oN, relativePrime, e, & d 
def RSA(p, q):
    n = p * q #Calculate the product of two primes
    oN = ((p - 1) * (q - 1)) #find a number that is relatively prime to this number
    relativePrimes = [] #List of numbers to test for eulers theorem

    #Appends the relative primes to a list called relativePrimes
    for e in range (2, oN):
        print("Working out the possible relative Primes...", int((e / oN) * 100), "%")
        checkList = []

        result = e / n
        if result.is_integer() == True:
            checkList.append(False)
        else:
            checkList.append(True)

        result = e / p
        if result.is_integer() == True:
            checkList.append(False)
        else:
            checkList.append(True)

        result = e / q
        if result.is_integer() == True:
            checkList.append(False)
        else:
            checkList.append(True)

        result = oN / e
        if result.is_integer() == True:
            checkList.append(False)
        else:
            checkList.append(True)

        if all(checkList): #If all elements are True, e is a relativePrime, save it
            relativePrimes.append(e)


    #Check if a random relative prime, is eligible to be the secret value d aswell
    relativePrimes.sort()
    d = False #initiate d with False, so that d has to be found in order to return the variables required
    while d == False:
        randomNumber = int(random.random() * len(relativePrimes))
        d = dCheck(relativePrimes[randomNumber], oN, relativePrimes[-1])
        if d != False: #When d is found, we can return the values needed for encryption and decryption
            return relativePrimes, oN, n, d, int(relativePrimes[randomNumber]) #last value is e!



#   --> Returns d if found
#       d is any a value between 1 and the biggest relativePrime, that rule out 1 with eulers theorem
#       oN is a fixed value calculated from (p - 1) (p - 1), used in eulers theorem MODULO
#       e is a random, relative prime, Relative to p & q
#       condition is the biggest relativePrime found, you don't need to look past this prime
def dCheck(e, oN, condition):

    d = 1
    while d < condition: #Iterate untill the biggest relativePrime relativePrime[-1]
        if((d * e) % oN == 1): #Check if i is in common with e
            return d
        d += 1
    return False

#   --> Encrypt payload with public key
def encrypt(e, n, payload):
    return((payload**e)%n)

#   --> Decrypt payload with private key
def decrypt(d, n, payload):
    return((payload**d)%n)


def main():

    relativePrimes, oN, n, d, e = RSA(1733,1301) #p and q
    print(relativePrimes," << these are Relative Primes!\noN: ", oN,"n: ", n,"d: ", d,"e: ", e,"\n")
    payload = 2999
    print("Starting value" ,payload)
    payload = encrypt(e, n, payload)
    print("Encrypted: ",payload)
    payload = decrypt(d, n, payload)
    print("Decrypted",payload)

main()
