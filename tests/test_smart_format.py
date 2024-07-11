import unittest

class TestCurrencyFormatAdvanced(unittest.TestCase):

    def test_smart_formatting(self):
        from format_currency import format_currency
        
        # Test smart formatting for different number systems
        self.assertEqual(format_currency(1234567.89, currency_code='USD', number_format_system='global', smart_number_formatting=True), '$ 1.23 Million')
        self.assertEqual(format_currency(12345678.9, currency_code='INR', number_format_system='indian', smart_number_formatting=True), '₹ 1.23 Crore')
        self.assertEqual(format_currency(1234567890.12, currency_code='CNY', number_format_system='chinese', smart_number_formatting=True), '¥ 1.23 万亿')

    def test_symbol_at_end(self):
        from format_currency import format_currency
        
        # Test placing the currency symbol at the end
        self.assertEqual(format_currency(1234567.89, currency_code='USD', place_currency_symbol_at_end=True), '1,234,567.89 $')
        self.assertEqual(format_currency(1234567.89, currency_code='INR', place_currency_symbol_at_end=True), '12,34,567.89 ₹')
        self.assertEqual(format_currency(1234567.89, currency_code='CNY', place_currency_symbol_at_end=True), '123,4567.89 ¥')

    def test_decimal_places(self):
        from format_currency import format_currency
        
        # Test different decimal places
        self.assertEqual(format_currency(1234567.89, currency_code='USD', decimal_places=0), '$ 1,234,568')
        self.assertEqual(format_currency(1234567.89, currency_code='INR', decimal_places=1), '₹ 12,34,567.9')
        self.assertEqual(format_currency(1234567.89123, currency_code='CNY', decimal_places=4), '¥ 123,4567.8912')

    def test_number_format_system(self):
        from format_currency import format_currency
        
        # Test different number format systems
        self.assertEqual(format_currency(1234567.89, currency_code='USD', number_format_system='global'), '$ 1,234,567.89')
        self.assertEqual(format_currency(1234567.89, currency_code='INR', number_format_system='indian'), '₹ 12,34,567.89')
        self.assertEqual(format_currency(1234567.89, currency_code='CNY', number_format_system='chinese'), '¥ 123,4567.89')

    def test_combined_features(self):
        from format_currency import format_currency
        
        # Test combination of smart formatting and placing symbol at end
        self.assertEqual(format_currency(1234567.89, currency_code='USD', smart_number_formatting=True, place_currency_symbol_at_end=True), '1.23 Million $')
        self.assertEqual(format_currency(12345678.9, currency_code='INR', number_format_system='indian', smart_number_formatting=True, place_currency_symbol_at_end=True), '1.23 Crore ₹')
        self.assertEqual(format_currency(1234567890.12, currency_code='CNY', number_format_system='chinese', smart_number_formatting=True, place_currency_symbol_at_end=True), '1.23 万亿 ¥')

        # Test combination of decimal places and different number format systems
        self.assertEqual(format_currency(1234567.89123, currency_code='USD', decimal_places=3, number_format_system='global'), '$ 1,234,567.891')
        self.assertEqual(format_currency(1234567.89123, currency_code='INR', decimal_places=1, number_format_system='indian'), '₹ 12,34,567.9')
        self.assertEqual(format_currency(1234567890.1234, currency_code='CNY', decimal_places=2, number_format_system='chinese'), '¥ 12,3456,7890.12')

    def test_invalid_number_format_system(self):
        from format_currency import format_currency
        
        # Test invalid number format system
        with self.assertRaises(ValueError):
            format_currency(1234567.89, currency_code='USD', number_format_system='invalid')

    def test_unexpected_kwargs(self):
        from format_currency import format_currency
        
        # Test unexpected keyword arguments
        with self.assertRaises(TypeError):
            format_currency(1234567.89, currency_code='USD', unexpected_kwarg=True)
