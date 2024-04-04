"""
This script will scrape the sprites of the Pokemon from the website Pokexperto.net and save them in a folder called "sprites".
"""
# Import the necessary libraries
import os
import requests
import pandas as pd

# Load the text file that contains the data of the Pokemon necessary to scrape the sprites
df = pd.read_csv('pokemon.csv')

# Create a folder to store the sprites
if os.path.exists('sprites') == False:
    os.mkdir('sprites')

# Create a function that will fix the truncation of the zeros in the Pokemon number
def fix_trunc_zeros(val):
    # Convert the value to a string
    val_str = str(val)
    
    # Check the length of the string
    if len(val_str) < 3:
        # Add leading zeros to the string until it reaches three characters
        val_str = val_str.zfill(3)
    
    # Return the corrected value
    return val_str

# Loop through the Pokemon numbers and scrape the sprites
for poke in df['#']:
    # Create the URL to scrape the sprite
    url = r'https://www.pokexperto.net/3ds/sprites/icon/{}.png'.format(fix_trunc_zeros(poke))
    # Make the request
    response = requests.get(url)
    # Save the image
    file = open('sprites/poke_{}.png'.format(poke), "wb")
    file.write(response.content)
    file.close()