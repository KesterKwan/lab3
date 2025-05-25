import price_info as price

def total_cost_shopping():
    cost=46.75
    result=price.total_cost_shopping()
    assert (cost == result)


def cost_of_fruit():

    fruits=13
    result=price.cost_of_fruits('watermelon',2)
    
    assert (fruits == result)

