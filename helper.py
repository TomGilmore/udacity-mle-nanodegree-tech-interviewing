class Node(object):
	
	def __init__(self, data):
		self.data = data
		self.next = None



class GNode(object):
	def __init__(self, value):
		self.value = value
		self.edges = []



class Graph(object):
	def __init__(self, nodes=[], edges=[]):
		self.nodes = nodes
		self.edges = edges
	
	def insert_node(self, new_node_val):
		new_node = GNode(new_node_val)
		self.nodes.append(new_node)
	
	def insert_edge(self, new_edge_val, node_from_val, node_to_val):
		from_found = None
		to_found = None
		for node in self.nodes:
			if node_from_val == node.value:
				from_found = node
			if node_to_val == node.value:
				to_found = node
		if from_found is None:
			from_found = GNode(node_from_val)
			self.nodes.append(from_found)
		if to_found is None:
			to_found = GNode(node_to_val)
			self.nodes.append(to_found)
		new_edge = Edge(new_edge_val, from_found, to_found)
		from_found.edges.append(new_edge)
		to_found.edges.append(new_edge)
		self.edges.append(new_edge)
	
	def find_min_span(self):
		srtEdges = sorted(self.edges, key=lambda x: x.value)
		eDict = {}
		visited = []
		while len(srtEdges) > 0:
			e = srtEdges.pop(0)
			if e.node_from.value not in visited or e.node_to.value not in visited:
				eDict.setdefault(e.node_from.value, []).append((e.node_to.value, e.value))
				visited.append(e.node_from.value)
				visited.append(e.node_to.value)
		
		for ed in eDict.keys():
			to_nodes = [i for i, j in eDict[ed]]
			for n in to_nodes:
				if n in eDict.keys():
					to_nodes2 = [i for i, j in eDict[n]]
					if ed not in to_nodes2:
						for i, j in eDict[ed]:
							if i == n:
								val = j
						eDict[n].append((ed, j))
				else:
					for i, j in eDict[ed]:
						if i == n:
							val = j
					eDict[n] = [(ed, val)]
			eDict[ed] = sorted(eDict[ed], key=lambda x: x[0])
		return eDict


class Edge(object):
	def __init__(self, value, node_from, node_to):
		self.value = value
		self.node_from = node_from
		self.node_to = node_to


def parent(T, n):

        #return parent of n if it exists, otherwise return -1
        numrows = len(T)

        for i in range(numrows):
                if T[i][n] == 1:
                        return i
        return -1

