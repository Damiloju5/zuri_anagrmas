# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # turn the word to a list and a lower case
    word_list = list(word.lower())
    word_list.sort()

    # turn anagram word to list and a lowwer case too
    anagram_list = list(anagram.lower())

    anagram_list.sort()

    isAnagram = word_list == anagram_list
    return isAnagram


print(find_anagrams("hello", "check"))
print(find_anagrams("below", "elbow"))
print(find_anagrams("Elvis", "Lives"))
