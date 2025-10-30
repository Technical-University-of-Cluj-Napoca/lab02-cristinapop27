from bst import BST

if __name__ == "__main__":
    bst = BST("https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words.txt", url = True)
    print(bst.autocomplete("appl"))