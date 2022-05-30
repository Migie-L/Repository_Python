############### Blackjack Project #####################


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

from art import logo
print (logo)

import random

ace = 11
jack = 10
queen = 10
king = 10
cards = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king]



def sum_card(list, card_num):
  list.extend(random.choices(cards, k=card_num))
  print(list)
  print(sum(list))
  
  # IF TOTAL SCORE MORE 21, ACE : 11 → 1
  if sum(list) > 21:
    for i in list:
      if i == 11:
        list.remove(11)
        list.append(1)
        print(list)
        return sum(list)
        
  else:
    score = sum(list)
    print(list)
    return sum(list)



def hit_or_stand():
  print(f"In this moment, your cards are {user}, and the total scores are {sum(user)}.")
  add_card = input("Type 'Y' to hit another card, or type 'N' to stand:  ").lower()
  print(add_card)
  if add_card == "n":
    print(f"dealer's card are {dealer} now.")
    if sum(dealer) < 16:
      sum_card(dealer, 1)
      print(f"dealer is {dealer} and dealer_score is {sum(dealer)}") 
    
  else:
    sum_card(user, 1)
    print(f"user is {user} and user_score :{sum(user)}.")


hit_or_stand()
 

user = []
sum_card(user, 2)


dealer = []
sum_card(dealer, 2)
print(dealer[0])




continue_game = True
while True:
  if sum(user) == 21 or sum(dealer) == 21:
    if sum(user) == 21 and sum(dealer) == 21:
      print("You 2 both Blackjack! Draw!")
      break
    elif sum(user) == 21 and sum(dealer) != 21:
      print("Blackjack! You win!")  
      break
    else:
      print("Dealer Blackjack! You lose")
      break
    break
  elif sum(user) > 21 or sum(dealer) > 21:
    if sum(user) > 21 and sum(dealer) > 21:
      print(f"You both over 21. Draw!")
      break
    elif sum(user) > 21:
      print("over 21. you lose.")
      break
    elif sum(dealer) > 21:
      print("Dealer over 21. you win")
      break


###BUG need to be fix >>>      
  elif sum(user) < 21 and sum(dealer) < 21: 
    if sum(user) == sum(dealer):
      print(f"draw! you 2 are the same")
      break
    elif sum(user) > sum(dealer):
      print(f"Your scores are {sum(user)}, and dealer's are {sum(dealer)}. You are great than dealer, you Win!")
      break
    else:
      print(f"Your scores are {sum(user)}, and dealer's are {sum(dealer)}. You are smaller than dealer, you lose!")
      break


  
      
      
      
    








