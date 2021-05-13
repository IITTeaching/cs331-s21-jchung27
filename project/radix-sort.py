from unittest import TestCase   
import urllib.request

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    arr_of_words = book_to_words(book_url)

    longestWord = len(max(arr_of_words, key=len))
    
    for i in range(longestWord):
        arr_of_words = countSort(arr_of_words, i, longestWord-1)

    return arr_of_words
    

def countSort(arr, index, maxLength):
    output = [0 for i in range(len(arr))]

    count = [0 for i in range(128)]

    for word in arr:
        if maxLength - index < len(word):
            count[word maxLength - index]] += 1
        else:
            count[0] += 1
    
    for i in range(128):
        count[i] += count[i-1]
    
    for i in range(len(arr)-1, -1, -1):
        if maxLength - index < len(arr[i]):
            output[count[arr[i] maxLength - index]]-1] = arr[i]
            count[arr[i] maxLength - index]] -= 1
        else:
            output[count[0] - 1] = arr[i]
            count[0] -= 1 
    
    return output

