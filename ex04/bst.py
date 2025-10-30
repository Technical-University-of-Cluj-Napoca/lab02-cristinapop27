import urllib
from typing import List
from urllib import request


class Node:
    def __init__(self, data):
        self.word = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, source: str, **kwargs):
        url = kwargs.get('url', False)
        file = kwargs.get('file', False)

        if url:
            words = self._load_from_url(source)
        elif file:
            words = self._load_from_file(source)

        #words = [w.strip() for w in words if w.strip()]

        self.root = self._build_bst(words)

    @staticmethod
    def _load_from_url(url: str) -> List[str]:
        with request.urlopen(url) as response:
            data = response.read().decode('utf-8')
        return data.splitlines()

    @staticmethod
    def _load_from_file(file: str) -> List[str]:
        with open(file, 'r', encoding='utf-8') as f:
            return f.read().splitlines()

    def _build_bst(self, words: List[str]) -> Node:
        if not words:
            return None
        mid = len(words) // 2

        node = Node(words[mid])
        node.left = self._build_bst(words[:mid])
        node.right = self._build_bst(words[mid + 1:])
        return node

    def _collect(self, node: Node, prefix: str, results: List[str]) -> None:
        if node is None:
            return
        self._collect(node.left, prefix, results)
        if node.word.startswith(prefix):
            results.append(node.word)
        self._collect(node.right, prefix, results)

    def autocomplete(self, prefix: str) -> List[str]:
        results: List[str] = []
        self._collect(self.root, prefix, results)
        return results