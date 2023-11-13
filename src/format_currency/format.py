import locale

from .country import Country

def format_currency(number, country_code=None, currency_code=None, currency_symbol=None, decimal_separator=None, thousands_separator=None, decimal_places=None, use_current_locale=False):
    autoformat = True
    indian_numbering_system = False
    china_numbering_system = False

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

            country_code = country.alpha2
            currency_code = country.currency_code
            decimal_separator = country.currency_decimal_separator
            thousands_separator = country.currency_thousands_separator
            decimal_places = country.currency_decimal_place

    if country_code in ('IN', 'BD', 'NP', 'PK'):
        indian_numbering_system = True
 
    if country_code == 'CN':
        china_numbering_system = True
 
    if use_current_locale:
        localeconv = locale.localeconv()
        thousands_separator = localeconv.get('mon_thousands_sep', thousands_separator)
        decimal_separator = localeconv.get('mon_decimal_point', decimal_separator)

    formatting_precision = f'.0{decimal_places}f'
    formatting = '{:,' + formatting_precision + '}'

    # return formatting
    formatted_number = formatting.format(number)

    if (not use_current_locale) and indian_numbering_system:
        formatted_number = format_india_numbering_system(formatted_number)
    if (not use_current_locale) and china_numbering_system:
        formatted_number = format_china_numbering_system(formatted_number)

    formatted_number = formatted_number.replace('.', '_')
    formatted_number = formatted_number.replace(',', thousands_separator)
    formatted_number = formatted_number.replace('_', decimal_separator)
    return f'{currency_symbol} {formatted_number}'.strip()


def format_india_numbering_system(number_str):
    is_negative = number_str.startswith('-')

    if is_negative:
        number_str = number_str[1:]

    number_str = number_str.replace(',', '')
    s, *d = number_str.partition(".")
    r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
    result = "".join([r] + d)

    if is_negative:
        return '-' + result

    return result


def format_china_numbering_system(number_str):
    is_negative = number_str.startswith('-')

    if is_negative:
        number_str = number_str[1:]

    number_str = number_str.replace(',', '')
    s, *d = number_str.partition(".")
    r = ",".join([s[x-4:x] for x in range(-4, -len(s), -4)][::-1] + [s[-4:]])
    result = "".join([r] + d)

    if is_negative:
        return '-' + result

    return result
