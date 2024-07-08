import os, json

cached_countries_data = None
cached_countries_data_dict = {}
cached_countries_data_by_currency_code_dict = {}

class Country():
    """Country Data"""
    def __init__(self, name, alpha2, alpha3, currency_code, currency_name, currency_symbol, currency_decimal_separator, currency_thousands_separator, currency_decimal_place=2, flag_base64=None):
        super().__init__()
        self.name = name
        self.alpha2 = alpha2
        self.alpha3 = alpha3
        self.currency_code = currency_code
        self.currency_name = currency_name
        self.currency_symbol = currency_symbol
        self.currency_decimal_place = currency_decimal_place
        self.currency_decimal_separator = currency_decimal_separator
        self.currency_thousands_separator = currency_thousands_separator
        self.flag_base64 = flag_base64

    @classmethod
    def load_countries_data(cls):
        """Load countries data from json"""
        global cached_countries_data

        if cached_countries_data is not None:
            return cached_countries_data

        data_json_path = os.path.join(os.path.dirname(__file__), 'data', 'countries.json')
        data = None
        try:
            with open(data_json_path) as f:
                data = json.load(f)
        except UnicodeDecodeError as e:
            with open(data_json_path, encoding = 'utf-8') as f:
                data = json.load(f)

        cached_countries_data = data
        return data

    @classmethod
    def load_country(cls, country_code):
        """Find country by it's ISO code"""
        global cached_countries_data_dict
        cached = cached_countries_data_dict.get(country_code, None)
        if cached is not None:
            return cached

        data = cls.load_countries_data()

        for country_data in data:
            if country_data.get('isoAlpha2', None) == country_code.upper():
                currency_data = country_data.get('currency', {})

                country = cls(
                            name=country_data.get('name', ''),
                            alpha2=country_data.get('isoAlpha2', ''),
                            alpha3=country_data.get('isoAlpha3', ''),
                            flag_base64=country_data.get('flag', None),
                            currency_code=currency_data.get('code', ''),
                            currency_name=currency_data.get('name', ''),
                            currency_symbol=currency_data.get('symbol', ''),
                            currency_decimal_separator=currency_data.get('decimal', '.'),
                            currency_thousands_separator=currency_data.get('thousands', ','),
                            currency_decimal_place=currency_data.get('decimalPlaces', 2),
                           )
                cached_countries_data_dict[country_code] = country
                return country
        
    @classmethod
    def load_country_by_currency_code(cls, currency_code):
        """Find country by it's currency code"""
        global cached_countries_data_by_currency_code_dict
        cached = cached_countries_data_by_currency_code_dict.get(currency_code, None)
        if cached is not None:
            return cached

        data = cls.load_countries_data()

        for country_data in data:
            currency_data = country_data.get('currency')
            if currency_data and currency_data.get('code', None) == currency_code.upper():
                currency_data = country_data.get('currency', {})

                country = cls(
                            name=country_data.get('name', ''),
                            alpha2=country_data.get('isoAlpha2', ''),
                            alpha3=country_data.get('isoAlpha3', ''),
                            flag_base64=country_data.get('flag', None),
                            currency_code=currency_data.get('code', ''),
                            currency_name=currency_data.get('name', ''),
                            currency_symbol=currency_data.get('symbol', ''),
                            currency_decimal_separator=currency_data.get('decimal', '.'),
                            currency_thousands_separator=currency_data.get('thousands', ','),
                            currency_decimal_place=currency_data.get('decimalPlaces', 2),
                           )
                cached_countries_data_by_currency_code_dict[currency_code] = country
                return country
        