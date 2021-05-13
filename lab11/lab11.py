from unittest import TestCase
import random

def quicksort(lst,pivot_fn):
    qsort(lst,0,len(lst) - 1,pivot_fn)

def qsort(lst,low,high,pivot_fn):
    ### BEGIN SOLUTION
    if high <= low:
        return
    i = low
    j = high - 1
    pivot, pivot_idx = pivot_fn(lst, low, high)
    lst[high], lst[pivot_idx] = lst[pivot_idx], lst[high]
    pivot_idx = high
    while j > i:
        if lst[i] > pivot and lst[j] < pivot:
            if pivot_idx != -1:
                lst[i], lst[j], lst[pivot_idx] = lst[j], lst[pivot_idx], lst[i]
                pivot_idx = j
            else:
                lst[i], lst[j] = lst[j], lst[i]
        else:
            if lst[i] <= pivot:
                i += 1
            if lst[j] >= pivot:
                j -= 1
    if j+1 != high and lst[j+1] > pivot and lst[j] < pivot:
        j += 1
    if lst[j] > lst[pivot_idx]:
        lst[j], lst[pivot_idx] = lst[pivot_idx], lst[j]
        pivot_idx = j
    qsort(lst, low, pivot_idx-1, pivot_fn)
    qsort(lst, pivot_idx+1, high, pivot_fn)
    ### END SOLUTION

def pivot_first(lst,low,high):
    ### BEGIN SOLUTION
    return lst[low], low
    ### END SOLUTION

def pivot_random(lst,low,high):
    ### BEGIN SOLUTION
    idx = random.randint(low, high)
    return lst[idx], idx
    ### END SOLUTION

def pivot_median_of_three(lst,low,high):
    ### BEGIN SOLUTION
    mid = statistics.median([lst[low], lst[high], lst[(high+low)//2]])
    idx = -1
    if mid == lst[low]:
        idx = low
    elif mid == lst[high]:
        idx = high
    else:
        idx = (high+low)//2 
    return mid, idx
    ### END SOLUTION

################################################################################
# TEST CASES
################################################################################
def randomize_list(size):
    lst = list(range(0,size))
    for i in range(0,size):
        l = random.randrange(0,size)
        r = random.randrange(0,size)
        lst[l], lst[r] = lst[r], lst[l]
    return lst

def test_lists_with_pfn(pfn):
    lstsize = 20
    tc = TestCase()
    exp = list(range(0,lstsize))

    lst = list(range(0,lstsize))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    lst = list(reversed(range(0,lstsize)))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    for i in range(0,100):
        lst = randomize_list(lstsize)
        quicksort(lst, pfn)
        tc.assertEqual(lst,exp)

# 30 points
def test_first():
    test_lists_with_pfn(pivot_first)

# 30 points
def test_random():
    test_lists_with_pfn(pivot_random)

# 40 points
def test_median():
    test_lists_with_pfn(pivot_median_of_three)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_first,
              test_random,
              test_median]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
