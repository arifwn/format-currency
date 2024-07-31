# Format Numbers as Currencies

A no-frills currency formatting library that allows you to format numbers as currencies using various country and currency codes, with support for custom formatting options and locale settings. Ideal for applications requiring precise and locale-aware currency representations.

-----

**Table of Contents**

- [Installation](#installation)
- Usage
    - [Basic](#usage)
    - [Advance](#advanced-usage)
    - [Parameters](#parameters)
- [Testing](#testing)
- [License](#license)
- [References](#references)

## Installation

```console
pip install format-currency
```

## Usage

```python
from format_currency import format_currency

# Format currency by country code, using the selected country's local monetary number formatting
formatted = format_currency(1234567.89, 'US') # returns $ 1,234,567.89
formatted = format_currency(1234567.89, 'ID') # returns Rp 1.234.567,89

# Format currency by currency code
formatted = format_currency(1234567.89, currency_code='USD') # returns $ 1,234,567.89
formatted = format_currency(1234567.89, currency_code='IDR') # returns Rp 1.234.567,89

# Smart formatting
formatted = format_currency(1234567.89, country_code='CN', smart_number_formatting=True) # returns ¥ 123.46 万

# Format currency by country code, respecting global locale settings
import locale
locale.setlocale(locale.LC_ALL, '')

formatted = format_currency(1234567.89, 'US', use_current_locale=True) # returns $ 1,234,567.89
formatted = format_currency(1234567.89, 'ID', use_current_locale=True) # returns Rp 1,234,567.89
```

## Advanced Usage

```python
# Custom formatting options
formatted = format_currency(
    1234567.89,
    country_code='IN',
    decimal_places=3,
    number_format_system='indian',
    place_currency_symbol_at_end=True
) # returns 12,34,567.890 ₹

formatted = format_currency(
    1234567.89,
    currency_code='USD',
    smart_number_formatting=True
) # returns $ 1.23 million
```

## Parameters

* `number` (float): The numerical value to be formatted.
* `country_code` (str, optional): The country code to determine currency formatting rules. Defaults to None.
* `currency_code` (str, optional): The currency code to determine currency formatting rules. Defaults to None.
* `currency_symbol` (str, optional): The symbol to be used for the currency. Defaults to None.
* `decimal_separator` (str, optional): The character to use as a decimal separator. Defaults to None.
* `thousands_separator` (str, optional): The character to use as a thousands separator. Defaults to None.
* `use_current_locale` (bool, optional): Whether to use the current locale settings for formatting. Defaults to False.
* `place_currency_symbol_at_end` (bool, optional): Whether to place the currency symbol at the end of the formatted number. * Defaults to False.
* `decimal_places` (int, optional): The number of decimal places to display. Defaults to the country's settings or 2.
* `number_format_system` (str, optional): The numbering system to use. Supported values are 'international', 'indian', 'chinese', * 'auto', 'none'. Defaults to 'auto'.
* `smart_number_formatting` (bool, optional): If True, converts large numbers into readable formats like "1.23 million". Defaults * to False.

## Error Handling

Raises `TypeError` if unexpected keyword arguments are provided.

## Testing

Install dependencies:

```bash
python -m pip install --upgrade pip build hatch
```

Run the test runner:

```bash
./test_runner.sh
```

## License

`format-currency` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## References

- [Decimal separator](https://en.wikipedia.org/wiki/Decimal_separator)
