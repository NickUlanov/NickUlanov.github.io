import string
from cesar_art import art
print(art)
alfabet = string.ascii_lowercase + string.ascii_lowercase


def cesar(star_text, shift_amount, direction_encryption):
    end_text = ""
    shift_amount = shift_amount % 25
    if direction_encryption == "decrypt":
        shift_amount *= -1

    for letter in star_text:

        if letter not in alfabet:  # Добавляю символ без изменний
            end_text += letter

        elif letter in alfabet:
            end_text += alfabet[alfabet.index(letter) + shift_amount]

    print(f"The {direction_encryption}ed text is {end_text} ")


while True:
    choose_function = input('Type encrypt to encription message, or type decrypt to decrypt the text\n')
    text = list(input("Input you's message\n").lower())
    shift = int(input('Type the shift number:\n'))
    cesar(star_text=text, shift_amount=shift, direction_encryption=choose_function)

    question = input('Still encrypting ? y / n\n')
    if question in ['n', 'no', 'No', 'N']:
        print('Goodbye')
        break
    else:
        continue

