import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head(10),cart.head(10),checkout.head(10),purchase.head(10))

visits_cart_left = visits.merge(cart, how ='left')
#print(visits_cart_left,len(visits_cart_left))

how_many_left_after_visit=len(visits_cart_left[visits_cart_left.cart_time.isnull()])
print(how_many_left_after_visit)

percent_of_not_cart = (float(how_many_left_after_visit))/float(len(visits)) * 100
#print(percent_of_not_cart)

visits_checkout_left = cart.merge(checkout, how ='left')
#print(visits_checkout_left)
how_many_left_after_cart=len(visits_checkout_left[visits_checkout_left.checkout_time.isnull()])
print(how_many_left_after_cart)

percent_of_not_checkout = (float(how_many_left_after_cart))/float(len(visits_checkout_left)) * 100
#print(percent_of_not_checkout)

all_data = visits.merge(cart, how = 'left').merge(checkout,how = 'left').merge(purchase,how = 'left')
print(all_data.head(10))
how_many_left_after_checkout = len(all_data[all_data.purchase_time.isnull()])

percent_of_not_purchase = float(len(purchase))/float(how_many_left_after_checkout) * 100
print(percent_of_not_cart,percent_of_not_checkout,percent_of_not_purchase)

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
all_data['time_to_checkout'] = all_data.checkout_time - all_data.visit_time
all_data['time_to_	cart'] = all_data.cart_time - all_data.visit_time
print(all_data.head(10))
print(all_data.time_to_purchase.mean())
