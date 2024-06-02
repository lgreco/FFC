# Look up table with ICAO HEX XPDR codes indexed by tail number
import assets
import time

end_time = time.time()
begin_time = end_time - 96*60*60
print(f'{end_time=}; {begin_time=}')

for tail_number in assets.aircraft:
    icao_hex = assets.aircraft[tail_number]
    print(icao_hex)