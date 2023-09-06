def dfs(graph, start_node):
  """
  Perform depth-first search on a graph.

  Args:
    graph: A graph represented as a dictionary. The keys are nodes and the values
      are lists of adjacent nodes.
    start_node: The start node of the search.

  Returns:
    A list of nodes in the order they were visited.
  """

  visited = []
  stack = [start_node]

  while stack:
    node = stack.pop()
    if node not in visited:
      visited.append(node)
      stack.extend(graph[node])

  return visited

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": [],
    "F": []
}

path = dfs(graph, "A")

print(path)
