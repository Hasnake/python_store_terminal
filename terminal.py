# Include the Customer and Item classes here.

members = [
  Customer(1, 'Harry', 'July 31, 1980'),
  Customer(2, 'Ken', 'July 3, 1988')
]

items = [
  Item('Python Textbook', 13.99, 20),
  Item('MacBook', 1199.99, 15),
  Item('Extended Warranty', 49.99, 12)
]

# Order in this case will be a dictionary. This allows us to add items multiple times.
# Example: I add 3 items of the MacBook, then I add 1 item of the MacBook. The order will now contain 4 items of the Macbok
order = {}

def main():
  # Your code here.
  pass

if __name__ == "__main__":
    main()
