from Summarizer.Summarization import bart_summarizer, bert_summarizer, xlnet_summarizer, gpt2_summarizer, T5_summarizer

data = """
A greedy algorithm is a simple, intuitive algorithm that is used in optimization problems. 
The algorithm makes the optimal choice at each step as it attempts to find the overall optimal way to solve the entire problem. 
Greedy algorithms are quite successful in some problems, such as Huffman encoding which is used to compress data, or Dijkstra's 
algorithm, which is used to find the shortest path through a graph. However, in many problems, a greedy strategy does not 
produce an optimal solution. For example, in the animation below, the greedy algorithm seeks to find the path with the largest sum. 
It does this by selecting the largest available number at each step. The greedy algorithm fails to find the largest sum, however, 
because it makes decisions based only on the information it has at any one step, without regard to the overall problem.
To make a greedy algorithm, identify an optimal substructure or subproblem in the problem. Then, determine what the solution will 
include (for example, the largest sum, the shortest path, etc.). Create some sort of iterative way to go through all of the 
subproblems and build a solution.

"""

# Summarization using Bart
summary, scores = bart_summarizer(data)
print(summary)
print (scores)

# Summarization using Bert
summary, scores = bert_summarizer(data)
print(summary)
print (scores)

# Summarization using XLNet
summary, scores = xlnet_summarizer(data)
print(summary)
print (scores)

# Summarization using GPT2
summary, scores = gpt2_summarizer(data)
print(summary)
print (scores)

# Summarization using T5
summary, scores = T5_summarizer(data)
print(summary)
print (scores)