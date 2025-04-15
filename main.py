import art
import random
from game_data import data
print(art.logo)
score = 0
should_continue = True
acc_b = random.choice(data)

while should_continue:

    acc_a = acc_b
    acc_b = random.choice(data)

    if acc_a == acc_b:
        acc_b = random.choice(data)


    def format_data(account):
        account_name = account["name"]
        account_desc = account["description"]
        account_country = account ["country"]
        return f"{account_name}, a {account_desc}, from {account_country}"

    def check_answer(user_guess, a_followers, b_followers):
        if a_followers > b_followers:
            return user_guess == "a"
        else:
            return user_guess =="b"


    print(f"Compare A: {format_data(acc_a)}")
    print(art.vs)
    print(f"Against B: {format_data(acc_b)}")
    guess = input("Who has more followers? Type A or B.").lower()
    print("\n" * 20)

    a_follower = acc_a["follower_count"]
    b_follower = acc_b["follower_count"]
    is_correct = check_answer(guess, a_follower, b_follower)

    if is_correct:
        score += 1
        print(f"You're right!. Current score is {score}")
    else:
        print(f"sorry, that's wrong :( . Your score is {score}")
        should_continue = False