import unittest

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

    # TODO: Test Full Regex


if __name__ == '__main__':
    unittest.main()
