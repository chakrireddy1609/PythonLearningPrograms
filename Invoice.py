number_of_minutes = float(input("Enter the number of minutes :"))
number_of_texts = float(input("Enter the number of texts :"))
number_of_gb = float(input("Enter the number of GB consumed :"))

def invoice_with_discount(minutes,texts,gb):
    price = (minutes*1.3)+(texts*0.3)+(gb*2)
    price_with_vat = (price+3)*1.1
    price_with_discount = price_with_vat*0.95
    print("Invoice after discount is ",price_with_discount)

def invoice_without_discount(minutes,texts,gb):
    price = (minutes * 1.3) + (texts * 0.3) + (gb * 2)
    price_with_vat = (price + 3) * 1.1
    print("Invoice without discount is ", price_with_vat)

invoice_with_discount(number_of_minutes,number_of_texts,number_of_gb)
invoice_without_discount(number_of_minutes,number_of_texts,number_of_gb)


