from scripts.staircase import staircase


def test_staircase_n_1_returns_1():
    assert staircase(1) == 1


def test_staircase_n_2_returns_2():
    assert staircase(2) == 2


def test_staircase_n_3_returns_4():
    assert staircase(3) == 4


def test_staircase_n_4_returns_7():
    assert staircase(4) == 7


def test_staircase_n_5_returns_13():
    assert staircase(5) == 13


def test_staircase_n_20_returns_121415():
    assert staircase(20) == 121415
