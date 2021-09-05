from scripts.staircase import staircase_r


def test_staircase_n_1_returns_1():
    assert staircase_r(1) == 1


def test_staircase_r_n_2_returns_2():
    assert staircase_r(2) == 2


def test_staircase_r_n_3_returns_4():
    assert staircase_r(3) == 4


def test_staircase_r_n_4_returns_7():
    assert staircase_r(4) == 7


def test_staircase_r_n_5_returns_13():
    assert staircase_r(5) == 13


def test_staircase_r_n_20_returns_121415():
    assert staircase_r(20) == 121415
