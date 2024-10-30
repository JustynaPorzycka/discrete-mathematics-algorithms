# Investigating the Difference Between Algebraic Connectivity and Vertex Connectivity

## Project Overview
This project aims to explore the difference between algebraic connectivity `k(G)` and vertex connectivity `μ2(G)` in the context of random graphs, as outlined in Theorem 12.15. The project involves developing a program that generates random graphs based on specified parameters and calculates the maximum difference in connectivity measures.

## Objectives

1. **Analyze Connectivity Differences**: 
   Investigate the theoretical implications of the difference `k(G) - μ2(G)`. This analysis will focus on how these two measures of connectivity relate to the structure of random graphs.

2. **Generate Random Graphs**: 
   Create a program that generates a specified number of random graphs based on user-defined parameters, including the probability of edges `p` and the number of vertices. The program will compute the difference `k(G) - μ2(G)` for each generated graph and identify the graph exhibiting the largest difference.

3. **Implement Random Tree Generation**: 
   Develop a second part of the program to generate random trees. Unlike the graph generation process, which uses the `G(n, p)` model, the random trees will be generated using Prüfer codes. The program will similarly compute the difference `k(G) - μ2(G)` for each generated tree and find the tree with the maximum difference.
