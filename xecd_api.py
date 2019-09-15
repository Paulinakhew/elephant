from xecd_rates_client import XecdClient
# install using pip install xecd-rates-client or pip3 install xecd-rates-client
xecd = XecdClient('xe891090202', '8ht3qjhq8vnu0dbb91ai40p44b')

def usd_to(currency: str):
    return xecd.convert_from("USD", currency)['to'][0]['mid']

def cad_to(currency: str):
    return xecd.convert_from("CAD", currency)['to'][0]['mid']

def convert(currency1: str, currency2: str):
    return xecd.convert_from(currency1, currency2)['to'][0]['mid']
