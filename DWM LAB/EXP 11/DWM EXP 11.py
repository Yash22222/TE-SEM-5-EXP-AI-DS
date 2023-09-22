# -*- coding: utf-8 -*-

# -- Sheet --

# DWML EXP NO 11


import numpy as np

def hits_algorithm(adjacency_matrix, max_iterations=100, epsilon=1e-6):
    num_pages = adjacency_matrix.shape[0]
    
    # Initialize hub and authority scores
    hub_scores = np.ones(num_pages)
    authority_scores = np.ones(num_pages)
    
    for iteration in range(max_iterations):
        # Update authority scores
        new_authority_scores = np.dot(adjacency_matrix.T, hub_scores)
        
        # Update hub scores
        new_hub_scores = np.dot(adjacency_matrix, new_authority_scores)
        
        # Normalize scores
        new_authority_scores /= np.linalg.norm(new_authority_scores, 2)
        new_hub_scores /= np.linalg.norm(new_hub_scores, 2)
        
        # Check for convergence
        if np.sum(np.abs(new_authority_scores - authority_scores)) < epsilon and \
           np.sum(np.abs(new_hub_scores - hub_scores)) < epsilon:
            break
        
        authority_scores = new_authority_scores
        hub_scores = new_hub_scores
    
    return hub_scores, authority_scores

# Example usage
if __name__ == "__main__":
    # Define a simple web graph (adjacency matrix)
    web_graph = np.array([
        [0, 1, 1, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]
    ])
    
    # Calculate HITS scores
    hub_scores, authority_scores = hits_algorithm(web_graph)
    
    # Print hub and authority scores
    print("Hub Scores:", hub_scores)
    print("Authority Scores:", authority_scores)

