# Game type: multiple choice
# Game setup
import random
import time
import inquirer


def choose(question, options):
    return inquirer.prompt(
        [
            inquirer.List(
                "select",
                message=question,
                choices=options,
            ),
        ]
    )["select"]


pscore = 0
cscore = 0
moves = ["scissors", "paper", "rock"]
def chose(quest):
    return inquirer.prompt(
        [
            inquirer.List(
                "select",
                message=quest,
                choices=moves,
            ),
        ]
    )["select"]
print(
    """
  _____   __  ____ _____ _____  ___   ____    _____     ____   ____  ____   ___  ____       ____   ___     __  __  _
 / ___/  /  ]|    / ___// ___/ /   \ |    \  / ___/    |    \ /    ||    \ /  _]|    \     |    \ /   \   /  ]|  |/ ]
(   \_  /  /  |  (   \_(   \_ |     ||  D  )(   \_     |  o  )  o  ||  o  )  [_ |  D  )    |  D  )     | /  / |  ' / 
 \__  |/  /   |  |\__  |\__  ||  O  ||    /  \__  |    |   _/|     ||   _/    _]|    /     |    /|  O  |/  /  |    \ 
 /  \ /   \_  |  |/  \ |/  \ ||     ||    \  /  \ |    |  |  |  _  ||  | |   [_ |    \     |    \|     /   \_ |     |
 \    \     | |  |\    |\    ||     ||  .  \ \    |    |  |  |  |  ||  | |     ||  .  \    |  .  \     \     ||  .  |
  \___|\____||____|\___| \___| \___/ |__|\_|  \___|    |__|  |__|__||__| |_____||__|\_|    |__|\_|\___/ \____||__|\_|
                                                                                                                    
"""
)
name = input("Whats your name? ")
print(f"Welcome to {name} vs computer, in scissors paper rock.")
print("Moves: scissors, paper, or rock.")
print("Rules: scissors cuts paper, paper covers rock, and rock smashes scissors.")
ans = choose("Would you like more info", "YN")
if ans == "Y":
    print(
        """After the round it will display what you play(left)
and what the computer plays(right) with hand notions of what they played:
         _______                    _______                  _______
    |---'   ____)____         |---'    ____)____        |---'   ____)
    |          ______)        |           ______)       |      (_____)
    |       __________)       |          _______)       |      (_____)
    |      (____)             |         _______)        |      (____)
    |---.__(___)              |---.__________)          |---.__(___)
"""
    )
print("Good luck!")
# Game start
ans = ('Y')
while ans == 'Y':
    pmove = chose('What is your move')
    cmove = random.choice(moves)
    if pmove == ("paper") and cmove == ("rock"):
        pscore = pscore + 1
        print(
            """
 __ __   ___   __ __      __    __   ___   ____   __
|  |  | /   \ |  |  |    |  |__|  | /   \ |    \ |  |    ________         ________
|  |  ||     ||  |  |    |  |  |  ||     ||  _  ||  |---'    ____)____   (____    '---
|  ~  ||  O  ||  |  |    |  |  |  ||  O  ||  |  ||__|           ______) (_____)
|___, ||     ||  :  |    |  `  '  ||     ||  |  | __           _______) (_____)
|     ||     ||     |     \      / |     ||  |  ||  |         _______)   (____)
|____/  \___/  \__,_|      \_/\_/   \___/ |__|__||__|---.__________)      (___)__.---
"""
        )
    if pmove == ("rock") and cmove == ("rock"):
        print(
            """
 ___    ____    ____  __    __  __
|   \  |    \  /    ||  |__|  ||  |    _______     ________
|    \ |  D  )|  o  ||  |  |  ||  |---'   ____)   (____    '---
|  D  ||    / |     ||  |  |  ||__|      (_____) (_____)
|     ||    \ |  _  ||  `  '  | __       (_____) (_____)
|     ||  .  \|  |  | \      / |  |      (____)   (____)
|_____||__|\_||__|__|  \_/\_/  |__|---.__(___)     (___)__.---
    """
        )
    if pmove == ("scissors") and cmove == ("rock"):
        cscore = cscore + 1
        print(
            """
    __   ___   ___ ___  ____  __ __  ______    ___  ____       __    __   ___   ____   __
   /  ] /   \ |   |   ||    \|  |  ||      |  /  _]|    \     |  |__|  | /   \ |    \ |  |    _______          ________
  /  / |     || _   _ ||  o  )  |  ||      | /  [_ |  D  )    |  |  |  ||     ||  _  ||  |---'   ____)____    (____    '---
 /  /  |  O  ||  \_/  ||   _/|  |  ||_|  |_||    _]|    /     |  |  |  ||  O  ||  |  ||__|          ______)  (_____)
/   \_ |     ||   |   ||  |  |  :  |  |  |  |   [_ |    \     |  `  '  ||     ||  |  | __        __________) (_____)
\     ||     ||   |   ||  |  |     |  |  |  |     ||  .  \     \      / |     ||  |  ||  |      (____)        (____)
 \____| \___/ |___|___||__|   \__,_|  |__|  |_____||__|\_|      \_/\_/   \___/ |__|__||__|---.__(___)          (___)__.---
    """
        )
    if pmove == ("scissors") and cmove == ("paper"):
        pscore = pscore + 1
        print(
            """
 __ __   ___   __ __      __    __   ___   ____   __ 
|  |  | /   \ |  |  |    |  |__|  | /   \ |    \ |  |    _______              _______
|  |  ||     ||  |  |    |  |  |  ||     ||  _  ||  |---'   ____)____    ____(____    '---
|  ~  ||  O  ||  |  |    |  |  |  ||  O  ||  |  ||__|          ______)  (______
|___, ||     ||  :  |    |  `  '  ||     ||  |  | __        __________) (_______
|     ||     ||     |     \      / |     ||  |  ||  |      (____)        (_______
|____/  \___/  \__,_|      \_/\_/   \___/ |__|__||__|---.__(___)           (__________.---
"""
        )
    if pmove == ("paper") and cmove == ("paper"):
        print(
            """
 ___    ____    ____  __    __  __ 
|   \  |    \  /    ||  |__|  ||  |    ________                _______
|    \ |  D  )|  o  ||  |  |  ||  |---'    ____)____     ____(____    '---
|  D  ||    / |     ||  |  |  ||__|           ______)   (______
|     ||    \ |  _  ||  `  '  | __           _______)   (_______
|     ||  .  \|  |  | \      / |  |         _______)     (_______
|_____||__|\_||__|__|  \_/\_/  |__|---.__________)         (__________.---
    """
        )
    if pmove == ("rock") and cmove == ("paper"):
        cscore = cscore + 1
        print(
            """
    __   ___   ___ ___  ____  __ __  ______    ___  ____       __    __   ___   ____   __ 
   /  ] /   \ |   |   ||    \|  |  ||      |  /  _]|    \     |  |__|  | /   \ |    \ |  |    _______         _______
  /  / |     || _   _ ||  o  )  |  ||      | /  [_ |  D  )    |  |  |  ||     ||  _  ||  |---'   ____)   ____(____    '---
 /  /  |  O  ||  \_/  ||   _/|  |  ||_|  |_||    _]|    /     |  |  |  ||  O  ||  |  ||__|      (_____) (______
/   \_ |     ||   |   ||  |  |  :  |  |  |  |   [_ |    \     |  `  '  ||     ||  |  | __       (_____) (_______
\     ||     ||   |   ||  |  |     |  |  |  |     ||  .  \     \      / |     ||  |  ||  |      (____)   (_______
 \____| \___/ |___|___||__|   \__,_|  |__|  |_____||__|\_|      \_/\_/   \___/ |__|__||__|---.__(___)      (__________.---
    """
        )
    if pmove == ("rock") and cmove == ("scissors"):
        pscore = pscore + 1
        print(
            """
 __ __   ___   __ __      __    __   ___   ____   __ 
|  |  | /   \ |  |  |    |  |__|  | /   \ |    \ |  |    _______          _______
|  |  ||     ||  |  |    |  |  |  ||     ||  _  ||  |---'   ____)    ____(____   '---
|  ~  ||  O  ||  |  |    |  |  |  ||  O  ||  |  ||__|      (_____)  (______
|___, ||     ||  :  |    |  `  '  ||     ||  |  | __       (_____) (__________
|     ||     ||     |     \      / |     ||  |  ||  |      (____)        (____)
|____/  \___/  \__,_|      \_/\_/   \___/ |__|__||__|---.__(___)          (___)__.---
"""
        )
    if pmove == ("scissors") and cmove == ("scissors"):
        print(
            """
 ___    ____    ____  __    __  __ 
|   \  |    \  /    ||  |__|  ||  |    _______               _______
|    \ |  D  )|  o  ||  |  |  ||  |---'   ____)____     ____(____   '---
|  D  ||    / |     ||  |  |  ||__|          ______)   (______
|     ||    \ |  _  ||  `  '  | __        __________) (__________
|     ||  .  \|  |  | \      / |  |      (____)             (____)
|_____||__|\_||__|__|  \_/\_/  |__|---.__(___)               (___)__.---
    """
        )
    if pmove == ("paper") and cmove == ("scissors"):
        cscore = cscore + 1
        print(
            """ 
    __   ___   ___ ___  ____  __ __  ______    ___  ____       __    __   ___   ____   __ 
   /  ] /   \ |   |   ||    \|  |  ||      |  /  _]|    \     |  |__|  | /   \ |    \ |  |     _______              _______
  /  / |     || _   _ ||  o  )  |  ||      | /  [_ |  D  )    |  |  |  ||     ||  _  ||  |---'    ____)____    ____(____   '---
 /  /  |  O  ||  \_/  ||   _/|  |  ||_|  |_||    _]|    /     |  |  |  ||  O  ||  |  ||__|           ______)  (______
/   \_ |     ||   |   ||  |  |  :  |  |  |  |   [_ |    \     |  `  '  ||     ||  |  | __           _______) (__________
\     ||     ||   |   ||  |  |     |  |  |  |     ||  .  \     \      / |     ||  |  ||  |         _______)        (____)
 \____| \___/ |___|___||__|   \__,_|  |__|  |_____||__|\_|      \_/\_/   \___/ |__|__||__|---.__________)           (___)__.---
    """
        )
    print(f"{name}-{pscore} computer-{cscore}")
    ans = choose('Would you like to keep playing?', 'YN')
time.sleep(1)
# End text
if pscore > cscore:
    print(
        """
 __ __   ___   __ __      __    __   ___   ____       ______  __ __    ___       ____   ____  ___ ___    ___  __
|  |  | /   \ |  |  |    |  |__|  | /   \ |    \     |      ||  |  |  /  _]     /    | /    ||   |   |  /  _]|  |
|  |  ||     ||  |  |    |  |  |  ||     ||  _  |    |      ||  |  | /  [_     |   __||  o  || _   _ | /  [_ |  |
|  ~  ||  O  ||  |  |    |  |  |  ||  O  ||  |  |    |_|  |_||  _  ||    _]    |  |  ||     ||  \_/  ||    _]|__|
|___, ||     ||  :  |    |  `  '  ||     ||  |  |      |  |  |  |  ||   [_     |  |_ ||  _  ||   |   ||   [_  __
|     ||     ||     |     \      / |     ||  |  |      |  |  |  |  ||     |    |     ||  |  ||   |   ||     ||  |
|____/  \___/  \__,_|      \_/\_/   \___/ |__|__|      |__|  |__|__||_____|    |___,_||__|__||___|___||_____||__|
  """
    )
elif pscore < cscore:
    print(
        """
 __ __   ___   __ __      _       ___   _____ ______      ______  __ __    ___       ____   ____  ___ ___    ___  __
|  |  | /   \ |  |  |    | |     /   \ / ___/|      |    |      ||  |  |  /  _]     /    | /    ||   |   |  /  _]|  |
|  |  ||     ||  |  |    | |    |     (   \_ |      |    |      ||  |  | /  [_     |   __||  o  || _   _ | /  [_ |  |
|  ~  ||  O  ||  |  |    | |___ |  O  |\__  ||_|  |_|    |_|  |_||  _  ||    _]    |  |  ||     ||  \_/  ||    _]|__|
|___, ||     ||  :  |    |     ||     |/  \ |  |  |        |  |  |  |  ||   [_     |  |_ ||  _  ||   |   ||   [_  __
|     ||     ||     |    |     ||     |\    |  |  |        |  |  |  |  ||     |    |     ||  |  ||   |   ||     ||  |
|____/  \___/  \__,_|    |_____| \___/  \___|  |__|        |__|  |__|__||_____|    |___,_||__|__||___|___||_____||__|
  """
    )
else:
    print(
        """
 __ __   ___   __ __      ______  ____    ___  ___        ______  __ __    ___       ____   ____  ___ ___    ___  __
|  |  | /   \ |  |  |    |      ||    |  /  _]|   \      |      ||  |  |  /  _]     /    | /    ||   |   |  /  _]|  |
|  |  ||     ||  |  |    |      | |  |  /  [_ |    \     |      ||  |  | /  [_     |   __||  o  || _   _ | /  [_ |  |
|  ~  ||  O  ||  |  |    |_|  |_| |  | |    _]|  D  |    |_|  |_||  _  ||    _]    |  |  ||     ||  \_/  ||    _]|__|
|___, ||     ||  :  |      |  |   |  | |   [_ |     |      |  |  |  |  ||   [_     |  |_ ||  _  ||   |   ||   [_  __
|     ||     ||     |      |  |   |  | |     ||     |      |  |  |  |  ||     |    |     ||  |  ||   |   ||     ||  |
|____/  \___/  \__,_|      |__|  |____||_____||_____|      |__|  |__|__||_____|    |___,_||__|__||___|___||_____||__|
  """
    )
time.sleep(3)
print(
    """
 ______  __ __   ____  ____   __  _ _____     _____   ___   ____       ____  _       ____  __ __  ____  ____    ____
|      ||  |  | /    ||    \ |  |/ ] ___/    |     | /   \ |    \     |    \| |     /    ||  |  ||    ||    \  /    |
|      ||  |  ||  o  ||  _  ||  ' (   \_     |   __||     ||  D  )    |  o  ) |    |  o  ||  |  | |  | |  _  ||   __|
|_|  |_||  _  ||     ||  |  ||     \__  |    |  |_  |  O  ||    /     |   _/| |___ |     ||  ~  | |  | |  |  ||  |  |  ____
  |  |  |  |  ||  _  ||  |  ||     /  \ |    |   _] |     ||    \     |  |  |     ||  _  ||___, | |  | |  |  ||  |_ | |____|
  |  |  |  |  ||  |  ||  |  ||  .  \    |    |  |   |     ||  .  \    |  |  |     ||  |  ||     | |  | |  |  ||     |
  |__|  |__|__||__|__||__|__||__|\_|\___|    |__|    \___/ |__|\_|    |__|  |_____||__|__||____/ |____||__|__||___,_|

  _____   __  ____ _____ _____  ___   ____    _____     ____   ____  ____   ___  ____       ____   ___     __  __  _  __
 / ___/  /  ]|    / ___// ___/ /   \ |    \  / ___/    |    \ /    ||    \ /  _]|    \     |    \ /   \   /  ]|  |/ ]|  |
(   \_  /  /  |  (   \_(   \_ |     ||  D  )(   \_     |  o  )  o  ||  o  )  [_ |  D  )    |  D  )     | /  / |  ' / |  |
 \__  |/  /   |  |\__  |\__  ||  O  ||    /  \__  |    |   _/|     ||   _/    _]|    /     |    /|  O  |/  /  |    \ |__|
 /  \ /   \_  |  |/  \ |/  \ ||     ||    \  /  \ |    |  |  |  _  ||  | |   [_ |    \     |    \|     /   \_ |     | __
 \    \     | |  |\    |\    ||     ||  .  \ \    |    |  |  |  |  ||  | |     ||  .  \    |  .  \     \     ||  .  ||  |
  \___|\____||____|\___| \___| \___/ |__|\_|  \___|    |__|  |__|__||__| |_____||__|\_|    |__|\_|\___/ \____||__|\_||__|
                       _______                                     _______                               _______
                  |---'   ____)____                          |---'    ____)____                     |---'   ____)
                  |          ______)                         |           ______)                    |      (_____)
                  |       __________)                        |          _______)                    |      (_____)
                  |      (____)                              |         _______)                     |      (____)
                  |---.__(___)                               |---.__________)                       |---.__(___)
"""
)