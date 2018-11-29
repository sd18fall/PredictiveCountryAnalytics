import pdb

def cumulative_sum(L):
    """ returns a list where each element in the returned list is the
        cumulative sum of the elements up to the corresponding element in
    the original list.

    L: the original list
    returns: a new list where element i is equal to the sum of element
         0 through i in the original list """
    for i in range(len(L)):
        L[i] = L[i-1] + L[i]
        pdb.set_trace()
    return L

if __name__ == '__main__':
    print(cumulative_sum([1, 2, 3]))
