import addition


class TestAddition:
    def test_add_no_args(self):
        assert addition.add() == 0

    def test_add_one_arg(self):
        assert addition.add(5) == 5

    def test_add_two_args(self):
        assert addition.add(1, 2) == 3

    def test_add_three_args(self):
        assert addition.add(7, 1, 2) == 10

    def test_add_four_args(self):
        assert addition.add(6, 2, 4, 3) == 15