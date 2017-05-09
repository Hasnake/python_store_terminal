# Store Terminal

For this exercise, you will write a program that simulates a storefront. NOTE: The requirements are meant to be slightly vague as this project can go in any direction you can choose. The examples are merely a guideline.

First we will need to build some classes to handle all of our needs. We have the following types of classes we will need.

## Item

An item contains the following criteria:

* name (string)
* price (float)
* inventory (integer >= 0)

## Customer

A customer has the following criteria:

* Member Number (integer > 0)
* Name (string)
* Birthday (string)

# Storefront Interaction

The goal of the storefront is to successfully allow a user to complete a transaction. A starter file helps build each of the scenarios defined below.

## Identify the Customer

The following asks for a valid Member Number.

```
Welcome to MY STORE!

What is your Member Number? 5
I'm sorry. That is not a valid Member Number.

What is your Member Number? 2
Welcome Ken! What can I get for you?
```

## Offer choices to the user for items.

The interface will then allow you to select items from the list and help you decide what to get.

```
Welcome Ken! What can I get for you?

1. Python Textbook..........13.99
2. Macbook................1199.99
3. Extended Warranty........49.99

Which option would you like?
```

## Selecting an Item to add to Cart

Once a valid item is selected (via the number), it will then ask for the quantity.

```
Which option would you like? 4
I'm sorry. That is an invalid option.

Which option would you like? abc
I'm sorry. That is an invalid option.

Which option would you like? 1
How many of the Python Textbook would you like? -1
I'm sorry. That is an invalid option.

How many of the Python Textbook would you like? 2
Awesome! I added 2 of the Python Textbook to your cart.

Would you like to add more items (y/n)?
```
The user would go through the same flow offering choices to the user should the user select "y".

## Checkout

```
Would you like to add more items (y/n)? n

Here is your order:

Qty   Item                      Price
---   ----                      -----
2     Python Textbook           27.98

Subtotal                        27.98
Tax                              2.80
Total                           30.78

Is this correct? (y/n)
```

If the user says n, the user is directed back to the same flow offering choices to the user.

If the user says y, the user is directed to a final confirmation page.

```
Thank you! Come again.
```

# Bonuses

## Multiple Orders

Once an order is completed, allow a user to make a new order without exiting the application.

## Adding Inventory

Keep track of the inventory. That way, a user cannot select something the store does not have. Have orders reduce the inventory each time.

## Editing Item Qty

Sometimes, users specify the wrong number of items. Allow the user to edit them somehow (perhaps allowing negative quantity values etc.)

## Add your own.

So many ways you can go in this route.

* Allow "upcharges"
* Make the look of the page extra fancy.
* Save the data to files in Python.
* Offer a discount if it's the birthday.
