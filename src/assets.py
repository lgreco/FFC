# ICAO HEX codes for aircraft transponders
# Obtained from https://www.avionictools.com/icao.php
aircraft = {
    'N773SP': 'AA75CA', # Skyhawk
    'N41598': 'A4EA67', # Archer
    'N31401': 'A3581F', # Arrow
    'N700ZG': 'A956D4'  # Cirrus
 } 

user = 'lgreco'
password = 'foxflyingclub'

def get_icao_hex(tail_number):
    if aircraft[tail_number]: return aircraft[tail_number]
    return None
