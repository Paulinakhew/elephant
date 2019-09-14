from xecd_rates_client import XecdClient
xecd = XecdClient('xe891090202', '8ht3qjhq8vnu0dbb91ai40p44b')

def usd_to(currency: str):
    return xecd.convert_from("USD", currency)['to'][0]['mid']

def cad_to(currency: str):
    return xecd.convert_from("CAD", currency)['to'][0]['mid']
