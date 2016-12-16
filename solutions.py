import itertools
import helper
from helper import Node
from helper import Graph
from helper import Edge


'''
Question 1

Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" 
and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return 
a boolean True or False.
'''
def question1(s,t):
	
	if len(t) > len(s) or s is None or t is None:
		return False
		
	s = s.lower()
	t = t.lower()
	
	sDict = dict.fromkeys(s,0)
	tDict = dict.fromkeys(t,0)
	
	for i in range(len(s) - len(t)):
		check = dict.fromkeys( s[i:i+len(t)], 0 )
		
		if check == tDict:
			return True
	
	return False


'''
Question 2

Given a string a, find the longest palindromic substring contained in a. Your function definition should look 
like question2(a), and return a string.
'''
def question2(a):
	a = a.lower()
	if len(a) == 1:
		return a	# Smallest palidrone

	result = a[0:2]		# Initalize 'result' with next smallest potential palidrone
 	for i in range(len(a)):
		for j in range(i):
			chunk = a[j:i + 1]
			
			if chunk == chunk[::-1] and len(chunk) > len(result):
				result = chunk
		
	return result


'''
Question 3

Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all 
vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an 
adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}

Vertices are represented as unique strings. The function definition should be question3(G)
'''
def question3(G):
	if not isinstance(G, Graph):
		return 'Invalid input'	
	return G.find_min_span()

'''
Question 4

Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest 
node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on 
the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common 
ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The 
function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the 
index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative 
integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular 
order. 
'''
def question4(T, r, n1, n2):
	
	n1_ps = []
	
	while n1 != r:
		n1 = helper.parent(T, n1)
		n1_ps.append(n1)
	
	if len(n1_ps) == 0:
		return -1
	    
	while n2 != r:
		n2 = helper.parent(T, n2)
		
		if n2 in n1_ps:
			return n2
	
	return -1


'''
Question 5
Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 
elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), 
where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node 
class below to use as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
'''
def question5(ll, m):

	left_pointer = ll
	right_pointer = ll
	
	# Set right pointer at m nodes away from head
	for i in xrange(m-1):
	
		# Check for edge case of not having enough nodes
		if not right_pointer.next:
			return 'Error: m is larger than the linked list.'
		
		# Otherwise, set the block
		right_pointer = right_pointer.next
	
	while right_pointer.next:
		left_pointer = left_pointer.next
		right_pointer = right_pointer.next
	
	return left_pointer.data


# QUESTION 1 TEST CASES
print "QUESTION 1 TEST CASES:"
print question1('udacity', 'udacity1')
# Should print 'False'
print question1('udacity','ed')
# Should print 'False'
print question1('Udacity', 'ad')
# Should print 'True'
print question1('race car', 'Ace')
# Should print 'True'


# QUESTION 2 TEST CASES
print "\nQUESTION 2 TEST CASES:"
print question2('myracecar')
# Should print 'racecar'
print question2('aca')
# Should print 'aca'
print question2('aca aca')
# Should print 'aca aca')
print question2('zz')
# Should print 'zz'
print question2('o')
# Should print 'o'


# QUESTION 3 TEST CASES
print "\nQUESTION 3 TEST CASES:"
g = Graph()
g.insert_edge(1, 'A', 'B')
g.insert_edge(2, 'B', 'C')
g.insert_edge(3, 'C', 'B')
g.insert_edge(4, 'C', 'A')

print question3(g)
{'A': [('B', 1)], 'C': [('B', 2)], 'B': [('A', 1), ('C', 2)]}
print question3(None)
# Should print 'Invalid input'
print question3('aaaaa')
# Should print 'Invalid input'


# QUESTION 4 TEST CASES
print "\nQUESTION 4 TEST CASES:"
print question4([[0, 1, 0, 0, 0],
           	 [0, 0, 0, 0, 0],
           	 [0, 0, 0, 0, 0],
           	 [1, 0, 0, 0, 1],
           	 [0, 0, 0, 0, 0]],
          	  3,
          	  1,
          	  4)
# Should print 3
print question4([[0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                  3,
                  1,
                  2)
# Should print 0
print question4([[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]],
                  2,
                  3,
                  4)
# Should print 2


# QUESTION 5 TEST CASES

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print "\nQUESTION 5 TEST CASES"
print question5(a,2)
# Should print 5
print question5(a,1)
# Should print 6
print question5(a,10)
# Should raise an LookUpError message
print question5(a,6)
# Should print 1

