priceIsRight = 15

if (priceIsRight < 5):
    print("Price is too low!")
    if (priceIsRight >=5 and priceIsRight <= 9):
        print("Price is almost there!")
        if (priceIsRight == 10):
            print("Price is exactly that!")
else:
    print("Price is too high!")