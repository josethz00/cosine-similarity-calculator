def cosine_similarity(vector1: list[float], vector2: list[float]) -> float:
    """Returns the cosine of the angle between two vectors."""
    # the cosine similarity between two vectors is the dot product of the two vectors divided by the magnitude of each vector
    
    dot_product = 0
    largest_vector = vector1 if len(vector1) > len(vector2) else vector2