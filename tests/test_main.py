from src.main import find_in_matrix, get_platforms, is_palindrome


def test_plaindrome():
    assert True == is_palindrome(number=121)
    assert False == is_palindrome(number=-121)


def test_find_in_matrix():
    assert True == find_in_matrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
    )

    assert False == find_in_matrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=-1
    )


def test_get_platforms():

    assert 2 == get_platforms(
        trains=[
            [900, 910],
            [950, 1120],
            [1100, 1130],
            [1500, 1900],
            [1800, 2000],
        ]
    )

    assert 1 == get_platforms(trains=[[900, 910], [940, 1200]])
