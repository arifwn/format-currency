import unittest

class TestCurrencyFormat(unittest.TestCase):

    def test_currency_format_us(self):
        from format_currency import format_currency
        self.assertEqual(format_currency(1234567.89, 'US'), '$ 1,234,567.89')
        self.assertEqual(format_currency(1234567.89, currency_code='USD'), '$ 1,234,567.89')

        import locale
        locale.setlocale(locale.LC_ALL, '')
        self.assertEqual(format_currency(1234567.89, 'US', use_current_locale=True), '$ 1,234,567.89')
        self.assertEqual(format_currency(1234567.89, currency_code='USD', use_current_locale=True), '$ 1,234,567.89')

    def test_currency_format_id(self):
        from format_currency import format_currency
        self.assertEqual(format_currency(1234567.89, 'ID'), 'Rp 1.234.567,89')
        self.assertEqual(format_currency(1234567.89, currency_code='IDR'), 'Rp 1.234.567,89')

        import locale
        locale.setlocale(locale.LC_ALL, '')
        self.assertEqual(format_currency(1234567.89, 'ID', use_current_locale=True), 'Rp 1,234,567.89')
        self.assertEqual(format_currency(1234567.89, currency_code='IDR', use_current_locale=True), 'Rp 1,234,567.89')

    def test_currency_format_bh(self):
        from format_currency import format_currency
        self.assertEqual(format_currency(1234567.890, 'BH'), 'BHD 1,234,567.890')

        import locale
        locale.setlocale(locale.LC_ALL, '')
        self.assertEqual(format_currency(1234567.890, 'BH', use_current_locale=True), 'BHD 1,234,567.890')

    def test_currency_format_bi(self):
        from format_currency import format_currency
        self.assertEqual(format_currency(1234567.00, 'BI'), 'BIF 1,234,567')

        import locale
        locale.setlocale(locale.LC_ALL, '')
        self.assertEqual(format_currency(1234567.00, 'BI', use_current_locale=True), 'BIF 1,234,567')

    def test_load_country_not_found(self):
        from format_currency import format_currency
        self.assertEqual(format_currency(1234567.89, 'XX'), '1,234,567.89')
