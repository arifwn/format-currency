# Format Numbers as Currencies

A no-frill currency formatting library.

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install format-currency
```

## Usage

```python
from format_currency import format_currency

# format currency by country code, using the selected country's local monetary number formatting
formatted = format_currency(1234567.89, 'US') # returns $ 1,234,567.89
formatted = format_currency(1234567.89, 'ID') # returns Rp 1.234.567,89

#format currency by currency code
formatted = format_currency(1234567.89, currency_code='USD') # returns $ 1,234,567.89
formatted = format_currency(1234567.89, currency_code='IDR') # returns Rp 1.234.567,89


# format currency by country code, respecting global locale settings
import locale
locale.setlocale(locale.LC_ALL, '')

formatted = format_currency(1234567.89, 'US', use_current_locale=True) # returns $ 1,234,567.89
formatted = format_currency(1234567.89, 'ID', use_current_locale=True) # returns Rp 1,234,567.89

```

## License

`format-currency` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## References

- https://en.wikipedia.org/wiki/Decimal_separator
