from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        anagrams[key].append(word)

    return list(anagrams.values())

def main():
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print( strs1)
    print( group_anagrams(strs1))
    print()

    strs2 = [""]
    print( strs2)
    print(group_anagrams(strs2))
    print()

    strs3 = ["a"]
    print(strs3)
    print(group_anagrams(strs3))
    print()

    strs4 = ["abc", "bca", "cab", "abcd", "bcda", "a"]
    print( strs4)
    print(group_anagrams(strs4))
    print()

if __name__ == "__main__":
    main()
