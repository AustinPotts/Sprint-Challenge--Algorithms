'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # step 1. what is our base case? It would either be len of word == 0, since we have no word or it would be 
    #compare the len of the word to the "th" string so if its just t we still return 0
    # (the base case) if the length of the word is zero or less than "th" value we are done, we know our answer 
    # we can't use any loops so what would be ideal? A: If statements 
     
    # Base Case 
    if len(word) == 0 or len(word) < len("th"):
        return 0
    
    #slicing to obtain substring
    # if the first two letters of word are != to th then remove the first two values from the word recursively 
    if word[:2] != "th":
        return count_th(word[1:])
    # else add 1 then recurse removing the first two values
    else:
        return count_th(word[1:]) + 1

    
    pass
