def priceCheck(
    products, productPrices, productSold, soldPrice
    ):
        prodPricesDict = {products[i]: productPrices[i] for i in range(len(products))}
        errorQuantity = 0
        for i in range(len(productSold)):
            if soldPrice[i] != prodPricesDict[productSold[i]]:
                errorQuantity += 1
        
        return errorQuantity

print(priceCheck(
	products=['rice', 'sugar', 'wheat', 'cheese'],
	productPrices=[16.89, 56.92, 20.89, 345.99],
	productSold=['rice', 'cheese'],
	soldPrice=[18.99, 400.89]
))

print(priceCheck(
    products = ['eggs', 'milk', 'cheese'],
    productPrices = [2.89, 3.29, 5.79],
    productSold = ['eggs', 'eggs', 'cheese', 'milk'],
    soldPrice = [2.89, 2.99, 5.97, 3.29]
))
