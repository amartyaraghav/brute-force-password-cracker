import random
import pyautogui

char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~! @#$%^&*()_-+={[}]|;<,>.?/"
char_lis = list(char)

password = pyautogui.password("Enter your password:")

guess = ''
while (guess != password):
    guess = random.choices(char_lis,k=len(password))

    print(">>>>>"+str(guess)+"<<<<<")

    if (guess==list(password)):
        print("Your password is:"+"".join(guess))
        break