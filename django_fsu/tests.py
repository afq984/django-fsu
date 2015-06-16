import unittest
import re
import django_fsu


class PatternTest(unittest.TestCase):
    url = '/user/<username>/post/<int:post>'

    def testQuotePattern(self):
        self.assertSequenceEqual(
            ['username', 'int:post'],
            django_fsu.quote.findall(self.url)
        )

    def testQuoteSplit(self):
        self.assertSequenceEqual(
            ['/user/', 'username', '/post/', 'int:post', ''],
            django_fsu.quote.split(self.url)
        )

    def testIntRegex(self):
        self.assertEqual(
            r'(?P<post>\d+)',
            django_fsu.make_regex('int:post')
        )

    def testStringRegex(self):
        self.assertEqual(
            r'(?P<username>[^\/]+)',
            django_fsu.make_regex('username')
        )

    def _match(self, pat, tar):
        return re.match(django_fsu.route(pat), tar)

    def testRegexMatchText(self):
        self.assertTrue(self._match('<my_text>/', 'a string/'))

    def testRegexMatchInt(self):
        self.assertTrue(self._match('<int:my_int>/', '234532/'))

    def testRegexMatchFloat(self):
        self.assertTrue(self._match('<float:my_decimal>/', '234.35/'))

    def testRegexDoesntMatchFloatForInt(self):
        self.assertFalse(self._match('<int:my_int>/', '34.332/'))

    def testRegexMatchIntForFloat(self):
        self.assertTrue(self._match('<float:my_float>/', '2342/'))

    # TODO: Test Full Regex


if __name__ == '__main__':
    unittest.main()
