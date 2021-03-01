import random
import math
from replit import clear
from art import logo

check1 = True
while check1 is True:
  print(logo)
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand = random.choice(cards)
    return hand
  user_cards = []
  computer_cards = []
  for card in range(0,2):
    user_cards.append(deal_card())
  for card in range(0,2):
    computer_cards.append(deal_card())
  def calculate():
      calculate.user_score = 0
      calculate.computer_score = 0
  def calculate_score(user_cards1, computer_cards1):
    sum_of_user_cards = sum(user_cards1)
    sum_of_computer_cards = sum(computer_cards1)
    calculate()
    calculate.user_score += sum_of_user_cards
    calculate.computer_score += sum_of_computer_cards
    if calculate.user_score == 21:
      calculate.user_score = 0
      return calculate.user_score
    elif calculate.computer_score == 21:
      calculate.computer_score = 0
      return calculate.computer_score
    for card in user_cards1:
      if calculate.user_score > 21 and card == "11":
        user_cards1.remove("11")
        user_cards1.append("1")
      elif calculate.computer_score > 21 and card == "11":
        computer_cards1.remove("11")
        computer_cards1.append("1")      
  calculate_score(user_cards1=user_cards, computer_cards1=computer_cards)
  print(f"User score is: {calculate.user_score}")
  print(f"Computer score is: {calculate.computer_score}")
  def compare():
    print(f"User score is: {calculate.user_score}")
    print(f"Computer score is: {calculate.computer_score}")
    if calculate.user_score == calculate.computer_score:
      return print("It's a draw.")
    elif calculate.user_score == 21 or calculate.user_score == 0:
      return print("Player, you have won.")
    elif calculate.user_score > 21:
      return print("CPU has won.")
    elif calculate.computer_score == 21 or calculate.computer_score == 0:
      return print("CPU has won.")
    elif calculate.computer_score > 21:
      return print("Player, you have won.")
    elif calculate.user_score > calculate.computer_score and calculate.user_score < 21:
      return print("Player, you have won.")
    elif calculate.computer_score > calculate.user_score and calculate.computer_score < 21:
      return print("CPU has won.")
  check = True
  while check is True:
    if calculate.user_score == 21 or calculate.user_score == 0:
      print("Player, you have won.")
      restart = input("Do you want to restart the game? Press 'Y to restart, press 'n' to quit the game.\n").lower()
      if restart == "y":
        clear()
      elif restart == "n":
        check1 = False
      check = False
    elif calculate.user_score > 21:
      print("CPU has won.")
      restart = input("Do you want to restart the game? Press 'Y to restart, press 'n' to quit the game.\n").lower()
      if restart == "y":
        clear()
      elif restart == "n":
        check1 = False
      check = False
    elif calculate.computer_score == 21 or calculate.computer_score == 0:
      print("CPU has won.")
      restart = input("Do you want to restart the game? Press 'Y to restart, press 'n' to quit the game.\n").lower()
      if restart == "y":
        clear()
      elif restart == "n":
        check1 = False
      check = False
    elif calculate.computer_score > 21:
      print("Player, you have won.")
      restart = input("Do you want to restart the game? Press 'Y to restart, press 'n' to quit the game.\n").lower()
      if restart == "y":
        clear()
      elif restart == "n":
        check1 = False
      check = False
    else:
      draw_card = input("Player, do you want to draw a card again? Press 'Y' to draw, 'N' to end the game.\n").lower()
      if draw_card == "y":
        user_cards.append(deal_card())
        calculate_score(user_cards1=user_cards, computer_cards1=computer_cards)
        print(f"User score is: {calculate.user_score}")
        print(f"Computer score is: {calculate.computer_score}")
      elif draw_card == "n":
        print("Player will draw no more cards.")
        while calculate.computer_score < 17:
          computer_cards.append(deal_card())
          calculate_score(user_cards1=user_cards, computer_cards1=computer_cards)
          print("CPU has drawn a card.")
          print(f"Computer score is: {calculate.computer_score}")
        calculate_score(user_cards1=user_cards, computer_cards1=computer_cards)
        compare()
        check = False
        restart = input("Do you want to restart the game? Press 'Y to restart, press 'n' to quit the game.\n").lower()
        if restart == "y":
          clear()
        elif restart == "n":
          check1 = False
