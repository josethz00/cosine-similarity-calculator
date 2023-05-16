# Cosine Similarity Calculator

This repository contains a Python script that calculates the cosine similarity between two vectors. Cosine similarity is a measure of similarity between two vectors of an inner product space that measures the cosine of the angle between them.

## Cosine Similarity

Cosine similarity is a metric used to measure how similar two entities are, irrespective of their size. It measures the cosine of the angle between two vectors projected in a multi-dimensional space. 

In this context, the two vectors I am talking about are arrays of numbers (like a list in Python), and the angle between them is a measure of how similar they are. The closer the vectors, the smaller the angle, leading to a cosine close to 1, and vice versa. This metric is a measurement of orientation (not magnitude).

The mathematical formula for calculating cosine similarity is:

![Cosine Similarity Formula](https://latex.codecogs.com/svg.latex?%5Ctext%7BCosine%20Similarity%7D%20%3D%20%5Cfrac%7B%5Cvec%7BA%7D%20%5Ccdot%20%5Cvec%7BB%7D%7D%7B%5Cleft%20%5C%7C%20%5Cvec%7BA%7D%20%5Cright%20%5C%7C%20%5Cleft%20%5C%7C%20%5Cvec%7BB%7D%20%5Cright%20%5C%7C%7D)

Where:
- $A$ and $B$ are our vectors
- The dot product of $A$ and $B$ is calculated as $∑_{i=1}^{n} A[i] * B[i]$
- $||A||$ and $||B||$ are the magnitudes (lengths) of the vectors

The output will range from -1 to 1, where:
- 1 means the vectors are identical
- 0 means the vectors are orthogonal (not similar)
- -1 means the vectors are diametrically opposed (completely dissimilar)

### Code Explanation

The Python function `cosine_similarity(vector1: list[float], vector2: list[float]) -> float:` takes two vectors as input and calculates their cosine similarity.

The code begins by initializing the variables for dot product and magnitudes of the vectors. It then checks the lengths of the two input vectors and pads the shorter one with zeros so that they have the same length. This step is necessary for calculating the dot product.

Then, the dot product of the two vectors and the magnitude of each vector are calculated using for loops. Finally, the cosine similarity is calculated by dividing the dot product by the product of the magnitudes.

## Usage

You can use this function in your code as follows:

```python
from math import sqrt, pow

def cosine_similarity(vector1: list[float], vector2: list[float]) -> float:
    """Returns the cosine of the angle between two vectors."""
    # the cosine similarity between two vectors is the dot product of the two vectors divided by the magnitude of each vector
    
    dot_product = 0
    magnitude_vector1 = 0
    magnitude_vector2 = 0

    vector1_length = len(vector1)
    vector2_length = len(vector2)

    if vector1_length > vector2_length:
        # fill vector2 with 0s until it is the same length as vector1 (required for dot product)
        vector2 = vector2 + [0] * (vector1_length - vector2_length)
    elif vector2_length > vector1_length:


        # fill vector1 with 0s until it is the same length as vector2 (required for dot product)
        vector1 = vector1 + [0] * (vector2_length - vector1_length)

    # dot product calculation
    for i in range(len(vector1)):
        dot_product += vector1[i] * vector2[i]

    # vector1 magnitude calculation
    for i in range(len(vector1)):
        magnitude_vector1 += pow(vector1[i], 2)

    # vector2 magnitude calculation
    for i in range(len(vector2)):
        magnitude_vector2 += pow(vector2[i], 2)

    # final magnitude calculation
    magnitude = sqrt(magnitude_vector1) * sqrt(magnitude_vector2)

    # return cosine similarity
    return dot_product / magnitude

vector1 = [1, 2, 3]
vector2 = [2, 3, 4]
similarity = cosine_similarity(vector1, vector2)

print("The cosine similarity between vector1 and vector2 is: ", similarity)
```