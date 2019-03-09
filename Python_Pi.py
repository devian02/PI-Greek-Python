'''
Autor: xSklero
Version: 1.0 <09/03/19>

'''

dictionary = {}

def pi(n):
    ''' Method that calculates pi and saves it in a dictionary '''
    for x in range(1, n+1):
        cont = 1
        pi = 0

        for y in range(1, x+1):
            if y % 2 == 0:
                pi -= 4/cont
            else:
                pi += 4/cont
            cont += 2

        dictionary[x] = pi # Save current approximation in the dictionary



if __name__ == '__main__':

    n = int(input("Insert the numbers of approximations: "))
    pi(n) # Generating dictionary


    count = 1
    for x in range(1,n+1):
        print(count, " ----> ", end=" ")
        print(dictionary[x], "\n")
        count += 1


    input("\nPress enter to close..")
