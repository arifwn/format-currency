import unittest

class TestCurrencyFormat(unittest.TestCase):

    def test_currency_format_us(self):
        from format_currency import format_currency
        self.assertEqual(format_currency(1234567.89, 'US'), '$ 1,234,567.89')
        self.assertEqual(format_currency(1234567.89, currency_code='USD'), '$ 1,234,567.89')
        self.assertEqual(format_currency(1234567.89, 'us'), '$ 1,234,567.89')
        self.assertEqual(format_currency(1234567.89, currency_code='usd'), '$ 1,234,567.89')

        import locale
        locale.setlocale(locale.LC_ALL, '')
        self.assertEqual(format_currency(1234567.89, 'US', use_current_locale=True), '$ 1,234,567.89')
        self.assertEqual(format_currency(1234567.89, currency_code='USD', use_current_locale=True), '$ 1,234,567.89')

    def test_currency_format_id(self):
        from format_currency import format_currency
        self.assertEqual(format_currency(1234567.89, 'ID'), 'Rp 1.234.567,89')
        self.assertEqual(format_currency(-1234567.89, 'ID'), 'Rp -1.234.567,89')
        self.assertEqual(format_currency(1234567.89, currency_code='IDR'), 'Rp 1.234.567,89')
        self.assertEqual(format_currency(1234567.89, 'id'), 'Rp 1.234.567,89')
        self.assertEqual(format_currency(1234567.89, currency_code='idr'), 'Rp 1.234.567,89')

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

    def test_currency_format_in(self):
        import locale
        locale.setlocale(locale.LC_ALL, '')
        from format_currency import format_currency

        self.assertEqual(format_currency(1234567.891, 'IN'), '₹ 12,34,567.89')
        self.assertEqual(format_currency(-1234567.891, 'IN'), '₹ -12,34,567.89')
        self.assertEqual(format_currency(1234567.891, currency_code='INR'), '₹ 12,34,567.89')

        self.assertEqual(format_currency(1234567.891, 'IN', use_current_locale=True), '₹ 1,234,567.89')
        self.assertEqual(format_currency(1234567.891, currency_code='INR', use_current_locale=True), '₹ 1,234,567.89')

    def test_currency_format_cn(self):
        import locale
        locale.setlocale(locale.LC_ALL, '')
        from format_currency import format_currency

        self.assertEqual(format_currency(1234567.891, 'CN'), '¥ 123,4567.89')
        self.assertEqual(format_currency(123456789.123, 'CN'), '¥ 1,2345,6789.12')
        self.assertEqual(format_currency(12345678912345.123, 'CN'), '¥ 12,3456,7891,2345.12')
        self.assertEqual(format_currency(-1234567.891, 'CN'), '¥ -123,4567.89')
        self.assertEqual(format_currency(1234567.891, currency_code='CNY'), '¥ 123,4567.89')

        self.assertEqual(format_currency(1234567.891, 'CN', use_current_locale=True), '¥ 1,234,567.89')
        self.assertEqual(format_currency(1234567.891, currency_code='CNY', use_current_locale=True), '¥ 1,234,567.89')

    def test_load_country_not_found(self):
        from format_currency import format_currency
        self.assertEqual(format_currency(1234567.89, 'XX'), '1,234,567.89')
