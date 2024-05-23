############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

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

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
from art import logo
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0

  return sum(cards)
  if sum(cards)>21 and 11 in cards:
    cards.remove(11)
    cards.append(1)

def compare(user_score,comp_score):
  if user_score==compare:
    return "Its a draw"
  elif comp_score==0:
    return "You lose, oppenent has a blackjack"
  elif user_score==0:
    return "You win with a blackjack"
  elif user_score>21:
    return "You went over.you lose"
  elif comp_score>21:
    return "opp went over. You win"
  elif user_score>comp_score:
    return "You win"
  else:
    return "You lose"
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []
def play_game():

  print(logo)
  user_cards=[]
  comp_cards=[]
  is_game_over=False
  for i in range(2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card())
    
  while not is_game_over:
    user_score=calculate_score(user_cards)
    comp_score=calculate_score(comp_cards)
    print(f"Your cards:{user_cards},curent score:{user_score}")
    print(f"cmp cards:{comp_cards},curent score:{comp_score}")
    
    if user_score==0 or comp_score==0 or user_score>21:
      is_game_over=True
    else:
      user_shd_deal=input("Do you want to continue the game?")
      if user_shd_deal=='y':
        user_cards.append(deal_card())
      else:
        is_game_over=True
  
  while comp_score!=0 and comp_score<17:
    comp_cards.append(deal_card())
    comp_score=calculate_score(comp_cards)
  
  print(f"Your final hand:{user_cards}, final score:{user_score}")
  print(f"Computer's final hand:{comp_cards}, final score:{comp_score}")
  print(compare(user_score,comp_score))

while input("Do you want to play the game of blackjack?")=="y":
  play_game()
