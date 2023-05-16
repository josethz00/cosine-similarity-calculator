from cosine_similarity import cosine_similarity

def test_cosine_similarity():
    assert cosine_similarity([1, 2, 3], [1, 2, 3]) == 1
    print("Test 1 passed - cosine_similarity([1, 2, 3], [1, 2, 3]) == 1")

    assert cosine_similarity([1, 2, 3], [4, 5, 6]) == 0.9746318461970762
    print("Test 2 passed - cosine_similarity([1, 2, 3], [4, 5, 6]) == 0.9746318461970762")

    assert cosine_similarity([-1, -2, -3], [-4, -5, -6]) == 0.9746318461970762
    print("Test 3 passed - cosine_similarity([-1, -2, -3], [-4, -5, -6]) == 0.9746318461970762")

    assert cosine_similarity([1, 2, 3], [-4, -5, -6]) == -0.9746318461970762
    print("Test 4 passed - cosine_similarity([1, 2, 3], [-4, -5, -6]) == -0.9746318461970762")

    assert cosine_similarity([1, 2, 3], [1, 2, 3, 4, 5, 6]) == 0.3922322702763681
    print("Test 5 passed - cosine_similarity([1, 2, 3], [1, 2, 3, 4, 5, 6]) == 0.3922322702763681")

test_cosine_similarity()