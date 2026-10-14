incart_added_games = 10
new_games_tobe_added_incart = 5
print("current in-cart games: " ,incart_added_games, " new games added into the cart are",new_games_tobe_added_incart)

total_number_of_Games_inCart = incart_added_games + new_games_tobe_added_incart
print("the total number of games in cart: ",total_number_of_Games_inCart)

if(total_number_of_Games_inCart > 12):
    print("the store limit for adding games into your cart has been full... clean previous games and add new ones" \
          " purchase declined :/")
else:
    print("these games have been added to the cart successfully, enjoy^^^^")
    print("Receipt" \
                    "Total Cost : 1300RS each" \
                    f"Total games purchased : {total_number_of_Games_inCart} " \
                    "Purchase Successfull ...."  \
                          "for any inconvience contact epicgames@support.epic"  
        )