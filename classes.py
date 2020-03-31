import bisect
import sys
import os

class Node:
	def __init__(self):
		self.keys, self.children , self.is_leaf, self.next = [], [], True, None

	def splitNode(self):
		newNode = Node()

		if self.is_leaf:
			newNode.is_leaf = True
			midKey = self.keys[len(self.keys)/2]
			newNode.keys = self.keys[len(self.keys)/2:]
			newNode.children = self.children[len(self.keys)/2:]
			self.keys = self.keys[:len(self.keys)/2]
			self.children = self.children[:len(self.keys)/2]
			newNode.next = self.next
			self.next = newNode

		else:
			newNode.is_leaf = False
			midKey = self.keys[len(self.keys)/2]
			newNode.keys = self.keys[len(self.keys)/2+1:]
			newNode.children = self.children[len(self.keys)/2+1:]
			self.keys = self.keys[:len(self.keys)/2]
			self.children = self.children[:len(self.keys)/2 + 1]

		return midKey, newNode

class BPlusTree:
	def __init__(self, factor):
		self.factor, self.root = factor, Node()
		self.root.is_leaf, self.root.keys, self.root.children, self.root.next = True, [], [], None
	
	def insert_routine(self, key):
		ans, newNode =  self.tree_insert(key, self.root)

		if ans:
			newRoot = Node()
			newRoot.is_leaf, newRoot.keys, newRoot.children = False, [ans], [self.root, newNode]
			self.root = newRoot

	def tree_insert(self, key, node):

		if node.is_leaf:
			index = bisect.bisect(node.keys, key)
			node.keys[index:index] = node.children[index:index] = [key]
			return None, None if len(node.keys) <= self.factor-1 else node.splitNode()
		else:
			if key < node.keys[0]:
				ans, newNode = self.tree_insert(key, node.children[0])

			i = 0
			while i < range(len(node.keys) - 1):
				if key >= node.keys[i] and key < node.keys[i + 1]:
					arr = self.tree_insert(key, node.children[i+1])
					ans, newNode = arr[0], arr[1]
				i = i+1

			if key >= node.keys[-1]:
				arr = self.tree_insert(key, node.children[-1])
				ans, newNode = arr[0], arr[1]

		if ans:
			index = bisect.bisect(node.keys, ans)
			node.keys[index:index], node.children[index+1:index+1] = [ans], [newNode]
			return None, None if len(node.keys) <= self.factor-1 else node.splitNode()
		else:
			return None, None

	def tree_search_for_query(self, key, node):

		if node.is_leaf:
			return node

		else:
			if key <= node.keys[0]:
				return self.tree_search_for_query(key, node.children[0])

			i = 0
			while i < range(len(node.keys)-1):
				if key>node.keys[i]:
					if key<=node.keys[i+1]:
						return self.tree_search_for_query(key, node.children[i+1])
				i = i+1
			if key > node.keys[-1]:
				arr = self.tree_search_for_query(key, node.children[-1])
				return arr[0], arr[1]

	def count_query(self, key):

		count = 0
		start_leaf = self.tree_search_for_query(key, self.root)

		key_count, next_node = self.get_keys_in_range(key, key, start_leaf)
		count = count + key_count

		while next_node:
			key_count, next_node = self.get_keys_in_range(key, key, next_node)
			count = count + key_count

		return count

	def range_query(self, keyMin, keyMax):

		count = 0
		start_leaf = self.tree_search_for_query(keyMin, self.root)

		key_count, next_node = self.get_keys_in_range(keyMin, keyMax, start_leaf)
		count = count + key_count

		while next_node:
			key_count, next_node = self.get_keys_in_range(keyMin, keyMax, next_node)
			count = count + key_count

		return count

	def get_keys_in_range(self, keyMin, keyMax, node):

		count = 0
		for i in range(len(node.keys)):
			key = node.keys[i]
			if keyMin <= key:
				if key <= keyMax:
					count = count + 1

		if len(node.keys) == 0:
			return 0, None

		if node.keys[-1] > keyMax:
			next_node = None

		else:
			next_node = node.next if node.next else None
		return count, next_node