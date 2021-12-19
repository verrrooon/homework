import check_password as chpsw


class TestPassword:
    def test_password_min_length(self):
        assert chpsw.check('abcd') == False

    def test_password_more_than_six(self):
        assert chpsw.check('abcdefg') == False

    def test_password_num(self):
        assert chpsw.check('1234567') == False

    def test_password_more_than_six_with_num(self):
        assert chpsw.check('abcdefg1') == True

    def test_password_word(self):
        assert chpsw.check('PaSsword') == False

    def test_password_word2(self):
        assert chpsw.check('aPaSswordbd1') == False
