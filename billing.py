dict1={"categories":{
    "fruits":{
        "items":
                {"apple":60,"mango":100,"banana":200,"watermelon":60}
            },
    "vegetables":{
        "items":
                {"tomato":70,"potato":80,"beetroot":90,"brinjal":80}
                 }
    }
}

result = {


}
total = 0

items = list(dict1['categories'].keys())

while True:
    category=input(f"select the categories: {items} ")
    if category == 'exit':
        result['total_price'] = total
        print(result)
        break

    if category == 'fruits':
        fruit_items=list(dict1['categories']['fruits']['items'].keys())
        print(f"select the fruit items, {fruit_items}")
        item = input("select a item: ")
        # quantity = int(input("enter the quantity: "))
        new_item=fruit_items
        if item not in fruit_items:
            print("item not found")
            print(f"please select the item from the given list, {fruit_items}")
            item = input("select a item: ")


        quant = int(input("enter the quantity: "))
        price = dict1['categories']['fruits']['items'].get(item)
        total_price =price*quant
        print(total_price)

        if item in result:

            result[item]['quantity']=result[item]['quantity']+quant
            result[item]['price']=result[item]['price']+price



        else:
        # write into dict
            result[item] = {
                'quantity': quant,
                'price' : total_price
            }
        total = total+ total_price


    elif category =='vegetables':
        veg_items=list(dict1['categories']['vegetables']['items'].keys())
        print("select the vegetables items")
        print(veg_items)
        item=input("select a item:")
        new_item=veg_items


        if item not in veg_items:
            print("item not found")
            print(f"please select the item from the given list, {veg_items}")
            item = input("select a item: ")



        quantity=int(input("enter the quantity: "))
        price=dict1['categories']['vegetables']['items'].get(item)
        total_price=price*quantity
        print(total_price)

        if item in result:
            result[item]['quantity'] = result[item]['quantity'] + quantity
            result[item]['price'] = result[item]['price'] + price


        else:
            result[item] = {
            'quantity': quantity,
            'price': total_price
            }
        total=total+total_price



def fruits():




def vegetables():
