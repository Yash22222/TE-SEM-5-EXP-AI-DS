# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np

def pagerank(graph, damping_factor=0.85, max_iterations=100, epsilon=1e-6):
    # Number of web pages
    num_pages = len(graph)
    
    # Initialize page ranks with equal values
    page_ranks = np.ones(num_pages) / num_pages
    
    for iteration in range(max_iterations):
        new_page_ranks = np.zeros(num_pages)
        
        for i in range(num_pages):
            for j in range(num_pages):
                if graph[j, i] == 1:
                    # Page i links to page j
                    num_links = np.sum(graph[j])
                    new_page_ranks[i] += page_ranks[j] / num_links
        
        # Apply damping factor and calculate new page ranks
        new_page_ranks = (1 - damping_factor) / num_pages + damping_factor * new_page_ranks
        
        # Check for convergence
        if np.sum(np.abs(new_page_ranks - page_ranks)) < epsilon:
            break
        
        page_ranks = new_page_ranks
    
    return page_ranks

# Example usage
if __name__ == "__main__":
    # Define a simple web graph (adjacency matrix)
    web_graph = np.array([
        [0, 1, 1, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]
    ])
    
    # Calculate PageRank
    result = pagerank(web_graph)
    
    # Print the PageRank scores
    for i, rank in enumerate(result):
        print(f"Page {i+1}: {rank:.4f}")

