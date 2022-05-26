# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    #str1 = input("Enter 1st string: ")
    #str2 = input("Enter Second string: ")
    sorted_str1 = sorted(word)
    sorted_str2 = sorted(anagram)

    if sorted_str1 == sorted_str2:
        return True
    else:
        return False
    

print(find_anagram("below", "elbow"))

print(find_anagram("hello","check"))
    

