import os
import requests
import pandas as pd

df = pd.read_csv('pokemon.csv')

if os.path.exists('sprites') == False:
    os.mkdir('sprites')

def fix_trunc_zeros(val):
    # Convert the value to a string
    val_str = str(val)
    
    # Check the length of the string
    if len(val_str) < 3:
        # Add leading zeros to the string until it reaches three characters
        val_str = val_str.zfill(3)
    
    # Return the corrected value
    return val_str

for poke in df['#']:

    url = r'https://www.pokexperto.net/3ds/sprites/icon/{}.png'.format(fix_trunc_zeros(poke))
    response = requests.get(url)
    # Save the image
    file = open('sprites/poke_{}.png'.format(poke), "wb")
    file.write(response.content)
    file.close()