# incart_added_games = 10
# new_games_tobe_added_incart = 5
# print("current in-cart games: " ,incart_added_games, " new games added into the cart are",new_games_tobe_added_incart)

# total_number_of_Games_inCart = incart_added_games + new_games_tobe_added_incart
# print("the total number of games in cart: ",total_number_of_Games_inCart)

# if(total_number_of_Games_inCart > 12):
#     print("the store limit for adding games into your cart has been full... clean previous games and add new ones" \
#           " purchase declined :/")
# else:
#     print("these games have been added to the cart successfully, enjoy^^^^")
#     print("Receipt" \
#                     "Total Cost : 1300RS each" \
#                     f"Total games purchased : {total_number_of_Games_inCart} " \
#                     "Purchase Successfull ...."  \
#                           "for any inconvience contact epicgames@support.epic"  
#         )
a = 10
b = -a
print(a % a)

print(6//2)
print(5//2)

print(type(a) is type(b))
if type(a) == float:
    print("the value type is different")
else:
    print("calculating")
    print(a*2)
value = [1,2,3,4,5,6,7,8,9,20]
if type(value) == list:
    print("The value is a type of list so kinda working on it........ approving ")
    multiplier = 20
    divider_for_value = 20/35
    if divider_for_value > 0.09:
        print("The divider is being in used")
    else: 
        print("divider disapproved")
    value = [x * multiplier for x in value]
    print("the new approved list is: ",value)
else:
    print("de approving.")
    value = [-x for x in value]
    print(value)
