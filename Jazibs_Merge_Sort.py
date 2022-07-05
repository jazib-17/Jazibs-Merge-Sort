'''
   Jazib's Implementation of the Merge Sort Algorithm

   Author: Jazib Ahmed
   Email: jazib7537@gmail.com

   All my algorithms are done by looking at diagrams, no code is looked up.
'''

# Making an unsorted list example, this can be changed to sort any other list
unsorted = [769, 873, 932, 422, 908, 296, 786, 431, 442, 336, 806, 205, 265, 202, 525, 302, 670, 177, 254, 760, 824, 930, 423, 254, 867, 565, 763, 415, 657, 869, 399, 752, 665, 648, 952, 887, 783, 421, 928, 685, 937, 835, 191, 138, 151, 819, 329, 501, 562, 264, 50, 311, 795, 964, 516, 770, 939, 26, 804, 349, 493, 460, 329, 168, 555, 50, 749, 107, 751, 604, 784, 312, 412, 558, 346, 441, 774, 887, 367, 798, 386, 64, 485, 494, 606, 524, 477, 133, 913, 793, 926, 23, 179, 172, 397, 800, 343, 34, 597, 862]


def merge_sort(unsort):
    """
    This function uses the merge and formatter functions to merge sort the given
    parameter.
    """

    if len(unsort) < 2:
        return unsort

    # Making the unsorted list merge sort friendly by calling the formatter function.
    sort = formatter(unsort)

    # While loop that continues until the sort list contains only one element,
    # that is, all the items have been merged into one list/element.
    while len(sort) != 1:
        mergelist = []

        # Odd variable that will either be None or a list depending on if an odd
        # number of elements are being merged or not.
        odd = None

        # If statement that removes the odd list temporarily if the unsorted list
        # has an odd amount of numbers.
        if len(sort)%2 == 1:
            odd = sort[-1]
            sort = sort[:-1]

        # For loop that merges every 2 elements in the unsorted list.
        for i in range(0,len(sort),2):
            mergelist.append(merge(sort[i], sort[i+1]))

        # If statement that adds back the removed odd list if there is one.
        if odd != None:
            mergelist.append(odd)

        sort = mergelist

    # Returning the only element in the sorted list as it is the merge sorted list.
    return sort[0]

def formatter(list1):
    """
    This function formats a list by placing each of its contents into a list.
    Helpful for merging contents of an unsorted list.
    """
    formatlist = []
    for i in list1:
        formatlist.append([i])
    return formatlist

def merge(item1, item2):
    """
    This function merges two lists together into one ascending order list.
    """
    newlist = item1
    for j in item2:
        index,k = len(newlist),0
        while k < len(newlist):
            if j <= newlist[k]:
                index = k
                k = len(newlist)
            k+=1
        newlist.insert(index,j)
    return newlist

# Example: Calling on the merge_sort function to sort the list created at start.
sortlist = merge_sort(unsorted)
print(sortlist)

