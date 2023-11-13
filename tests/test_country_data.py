import unittest

class TestCountryData(unittest.TestCase):

    def test_load_country_us(self):
        from format_currency import Country
        country = Country.load_country('US')
        self.assertIsNotNone(country)
        self.assertEqual(country.name, 'United States')
        self.assertEqual(country.alpha2, 'US')
        self.assertEqual(country.alpha3, 'USA')
        self.assertEqual(country.currency_code, 'USD')
        self.assertEqual(country.currency_name, 'Dollar')
        self.assertEqual(country.currency_symbol, '$')
        self.assertEqual(country.currency_decimal_separator, '.')
        self.assertEqual(country.currency_thousands_separator, ',')
        self.assertEqual(country.currency_decimal_place, 2)

    def test_load_country_us_lowercase(self):
        from format_currency import Country
        country = Country.load_country('us')
        self.assertIsNotNone(country)
        self.assertEqual(country.name, 'United States')
        self.assertEqual(country.alpha2, 'US')
        self.assertEqual(country.alpha3, 'USA')
        self.assertEqual(country.currency_code, 'USD')
        self.assertEqual(country.currency_name, 'Dollar')
        self.assertEqual(country.currency_symbol, '$')
        self.assertEqual(country.currency_decimal_separator, '.')
        self.assertEqual(country.currency_thousands_separator, ',')
        self.assertEqual(country.currency_decimal_place, 2)

    def test_load_country_us_cached(self):
        from format_currency import Country
        country = Country.load_country('US')
        self.assertIsNotNone(country)
        self.assertEqual(country.name, 'United States')
        self.assertEqual(country.alpha2, 'US')
        self.assertEqual(country.alpha3, 'USA')
        self.assertEqual(country.currency_code, 'USD')
        self.assertEqual(country.currency_name, 'Dollar')
        self.assertEqual(country.currency_symbol, '$')
        self.assertEqual(country.currency_decimal_place, 2)

    def test_load_country_id(self):
        from format_currency import Country
        country = Country.load_country('ID')
        self.assertIsNotNone(country)
        self.assertEqual(country.name, 'Indonesia')
        self.assertEqual(country.alpha2, 'ID')
        self.assertEqual(country.alpha3, 'IDN')
        self.assertEqual(country.currency_code, 'IDR')
        self.assertEqual(country.currency_name, 'Rupiah')
        self.assertEqual(country.currency_symbol, 'Rp')
        self.assertEqual(country.currency_decimal_separator, ',')
        self.assertEqual(country.currency_thousands_separator, '.')
        self.assertEqual(country.currency_decimal_place, 2)

    def test_load_country_by_currency_code_usd(self):
        from format_currency import Country
        country = Country.load_country_by_currency_code('USD')
        self.assertIsNotNone(country)
        self.assertEqual(country.name, 'United States')
        self.assertEqual(country.alpha2, 'US')
        self.assertEqual(country.alpha3, 'USA')
        self.assertEqual(country.currency_code, 'USD')
        self.assertEqual(country.currency_name, 'Dollar')
        self.assertEqual(country.currency_symbol, '$')
        self.assertEqual(country.currency_decimal_separator, '.')
        self.assertEqual(country.currency_thousands_separator, ',')
        self.assertEqual(country.currency_decimal_place, 2)

    def test_load_country_by_currency_code_usd_lowercase(self):
        from format_currency import Country
        country = Country.load_country_by_currency_code('usd')
        self.assertIsNotNone(country)
        self.assertEqual(country.name, 'United States')
        self.assertEqual(country.alpha2, 'US')
        self.assertEqual(country.alpha3, 'USA')
        self.assertEqual(country.currency_code, 'USD')
        self.assertEqual(country.currency_name, 'Dollar')
        self.assertEqual(country.currency_symbol, '$')
        self.assertEqual(country.currency_decimal_separator, '.')
        self.assertEqual(country.currency_thousands_separator, ',')
        self.assertEqual(country.currency_decimal_place, 2)

    def test_load_country_bh(self):
        from format_currency import Country
        country = Country.load_country('BH')
        self.assertIsNotNone(country)
        self.assertEqual(country.name, 'Bahrain')
        self.assertEqual(country.alpha2, 'BH')
        self.assertEqual(country.alpha3, 'BHR')
        self.assertEqual(country.currency_code, 'BHD')
        self.assertEqual(country.currency_name, 'Dinar')
        self.assertEqual(country.currency_symbol, None)
        self.assertEqual(country.currency_decimal_separator, '.')
        self.assertEqual(country.currency_thousands_separator, ',')
        self.assertEqual(country.currency_decimal_place, 3)

    def test_load_country_not_found(self):
        from format_currency import Country
        country = Country.load_country('XX')
        self.assertIsNone(country)
