import pandas as pd
import pickle

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True
    
    def _dfs(self, node, prefix):
        if node.is_end:
            self.output.append((prefix + node.char))
        for child in node.children.values():
            self._dfs(child, prefix + node.char)

    def query(self, x):
        self.output = []
        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return[]
        self._dfs(node, x[:-1])

        return sorted(self.output, key=lambda x: x[1], reverse=True)


dataset = pd.read_csv("F:/LEARNING/Rebelway/PythonForProduction/Week02/titles.csv")
searchQuery = hou.pwd().parm("input").eval()

tr = Trie()
for title in dataset["title"]:
    tr.insert(str(title))

if searchQuery:
    res = tr.query(searchQuery.capitalize())
    # print(res)
    if res == []:
        print("No titles found")
    else:
        print(res)
else:
    print("Please enter a Movie Title in the input field")