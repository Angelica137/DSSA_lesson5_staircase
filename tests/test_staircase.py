from scripts.staircase import staircase


def test_staircase_n_1_returns_1():
    assert staircase(1) == 1


def test_staircase_n_2_returns_2():
    assert staircase(2) == 2
