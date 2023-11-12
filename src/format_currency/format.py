import locale

from .country import Country

def format_currency(number, country_code=None, currency_code=None, currency_symbol=None, decimal_separator=None, thousands_separator=None, decimal_places=None, use_current_locale=False):
    autoformat = True

    if currency_symbol or decimal_separator or thousands_separator:
        autoformat = False

    if autoformat:
        country = None
        currency_symbol = ''
        decimal_separator = '.'
        thousands_separator = ','
        decimal_places = 2

        if country_code:
            country = Country.load_country(country_code)
        if currency_code:
            country = Country.load_country_by_currency_code(currency_code)

        if country:
            if country.currency_symbol:
                currency_symbol = country.currency_symbol
            else:
                currency_symbol = country.currency_code

            decimal_separator = country.currency_decimal_separator
            thousands_separator = country.currency_thousands_separator
            decimal_places = country.currency_decimal_place
 
    if use_current_locale:
        localeconv = locale.localeconv()
        thousands_separator = localeconv.get('mon_thousands_sep', thousands_separator)
        decimal_separator = localeconv.get('mon_decimal_point', decimal_separator)

    formatting_precision = f'.0{decimal_places}f'
    formatting = '{:,' + formatting_precision + '}'

    # return formatting
    formatted_number = formatting.format(number)
    formatted_number = formatted_number.replace('.', '_')
    formatted_number = formatted_number.replace(',', thousands_separator)
    formatted_number = formatted_number.replace('_', decimal_separator)
    return f'{currency_symbol} {formatted_number}'.strip()

