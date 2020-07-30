def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

# print(search([1,2,3], 4))

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        print(L[size-i-1], e)
        if L[size-i-1] == e:
            return True
        #bound to be as l[i] referring to first element lol
        if L[i] < e:
            print(size)
            return False
    return False

# print(newsearch([1,2,3], 2))

def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
        print(i)
    print("Final L: ", L)

# modSwapSort([5,4,3,2,1])
def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
        print(i)
    print("Final L: ", L)
# swapSort([5,4,3,2,1])