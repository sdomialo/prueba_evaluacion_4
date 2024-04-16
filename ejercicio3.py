# Usando algoritmo dijkstra
# Desarrolle un algoritmo que implemente una red de ferrocarriles que conecten distintas ciudades y desvíos en la Tierra Media:

# Cada nodo del grafo no dirigido será una ciudad o un desvío, identificados con nombres o números.

# Encontrar la ruta más corta entre diferentes ciudades, como "Rivendell" a "Minas Tirith".
# Define the graph
graph = {
    'Rivendell': {'Minas Tirith': 10, 'Gondor': 15},
    'Minas Tirith': {'Rivendell': 10, 'Gondor': 20},
    'Gondor': {'Rivendell': 15, 'Minas Tirith': 20}
}

# Implement Dijkstra's algorithm
def dijkstra(graph, start, end):
    # Initialize the distance dictionary with infinity for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Initialize the visited set
    visited = set()

    # Start the algorithm
    while True:
        # Find the node with the minimum distance
        min_distance = float('inf')
        min_node = None
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        # If all nodes have been visited or the end node is reached, stop the algorithm
        if min_node is None or min_node == end:
            break

        # Update the distances of the neighboring nodes
        for neighbor, distance in graph[min_node].items():
            new_distance = distances[min_node] + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

        # Mark the current node as visited
        visited.add(min_node)

    # Return the shortest distance from start to end
    return distances[end]

# Find the shortest path from "Rivendell" to "Minas Tirith"
shortest_distance = dijkstra(graph, 'Rivendell', 'Minas Tirith')
print(f"The shortest distance from Rivendell to Minas Tirith is {shortest_distance}")
# Find the shortest path from "Minas Tirith" to "Gondor"
shortest_distance = dijkstra(graph, 'Minas Tirith', 'Gondor')
print(f"The shortest distance from Minas Tirith to Gondor is {shortest_distance}")