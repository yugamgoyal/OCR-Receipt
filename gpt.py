import pytesseract
from PIL import Image
import re

# Open the image and convert it to grayscale
image = Image.open('receipts/TargetBill.png')
image = image.convert('L')

# Extract the text from the image
text = pytesseract.image_to_string(image)

# Pre-process the text
text = text.lower()  # Convert to lowercase
text = re.sub(r'[^a-z0-9\n\.]', ' ', text)  # Replace all non-alphanumeric characters with spaces
text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single spaces

# Split the text into lines
lines = text.split('\n')

# Initialize the table with column headers
table = [["Item", "Price"]]

# Extract the item names and prices
for line in lines:
  if line:  # Skip empty lines
    # Split the line into words
    words = line.split(' ')

    # Find the index of the first numeric word (which should be the price)
    price_index = -1
    for i, word in enumerate(words):
      if word.isnumeric():
        price_index = i
        break

    # Extract the item name and price
    if price_index > 0:
      item = ' '.join(words[:price_index])
      price = ' '.join(words[price_index:])
      table.append([item, price])

# Print the table
for row in table:
  print(row)