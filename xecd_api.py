from xecd_rates_client import XecdClient
xecd = XecdClient('xe891090202', '8ht3qjhq8vnu0dbb91ai40p44b')
usd_to_cad=xecd.convert_from("USD", "CAD")['to'][0]['mid']
cad_to_usd=xecd.convert_from("CAD", "USD")['to'][0]['mid']
