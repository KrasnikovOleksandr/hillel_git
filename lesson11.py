from random import randint

number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
random_num = randint(0, 9)
letter_list = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'K', 'k',
               'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'V', 'v',
               'X', 'x', 'Y', 'y', 'Z', 'z']
random_letter = letter_list[randint(0, len(letter_list) - 1)]
symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']
random_symbol = symbol_list[randint(0, len(symbol_list) - 1)]

def password(letters=True, numbers=False, symbols=False, pass_lenght=8, duplicates=False):
  if pass_lenght < 8:
    print('Пароль менше 8 символів!!!')
    return None
  final_list = []
  if symbols:
    final_list += symbol_list
  if numbers:
    final_list += number_list
  if letters:
    final_list += letter_list

  counter = 0
  finnaly_password = ''
  while counter < pass_lenght:
    counter += 1
    random_letter = final_list[randint(0, len(letter_list))]
    finnaly_password += random_letter
    if duplicates:
      duplicates_1 = ''
      for i in finnaly_password:
        duplicates_1 += i
        if duplicates_1 == i:
          i = random_letter
  return finnaly_password

print(password(letters=True, numbers=True, symbols=False, pass_lenght=16, duplicates=True))