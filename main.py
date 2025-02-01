# import random
# import copy

# def create_bingo_card():
#     bingo_card = {}
#     step = 0
#     for char in 'BINGO':
#         bingo_card.update({char : random.sample(range(1+step, 15+step), k = 5)})
#         step += 15
#     return bingo_card

# def display_card(dict_card):
#     print('{:^3} {:^3} {:^3} {:^3} {:^3}'.format('B', 'I', 'N', 'G', 'O'))
#     for i in range(0,5):
#         row = list(item[i] 
#                     for item in dict_card.values())
#         print('{:^3} {:^3} {:^3} {:^3} {:^3}'.format(row[0], row[1], row[2], row[3], row[4]))

# def check_card(dict_card):
#     is_win = False
#     # check columns
#     for n_column in dict_card.values():
#         if is_win:
#             break
#         else:
#             for c in n_column:
#                 if c == 0:
#                     is_win = True
#                 else:
#                     is_win = False
#                     break
#     # check rows
#     if not is_win:
#         for i in range(len(dict_card.keys())):
#             if is_win:
#                 break
#             else:
#                 n_row = list(item[i] 
#                             for item in dict_card.values())
#                 for r in n_row:
#                     if r == 0:
#                         is_win = True
#                     else:
#                         is_win = False
#                         break
#     # check diagonals
#     if not is_win:
#         diagonal_1 = dict_card['B'][0], dict_card['I'][1], dict_card['N'][2], dict_card['G'][3], dict_card['O'][4]
#         for d in diagonal_1:
#             if d == 0:
#                 is_win = True
#             else:
#                 is_win = False    
#                 diagonal_2 = dict_card['B'][4], dict_card['I'][3], dict_card['N'][2], dict_card['G'][1], dict_card['O'][0]
#                 for d in diagonal_2:
#                     if d == 0:
#                         is_win = True
#                     else:
#                         is_win = False
#                         break
#                 break    
#     return is_win

# def cross_num(dict_card, called_num):
#     for list_num in dict_card.values():
#         for n in range(len(list_num)):
#             if list_num[n] == called_num:
#                 list_num[n] = 0
#                 break
#     return dict_card

# my_bingo_card = create_bingo_card()
# copy_card = copy.deepcopy(my_bingo_card)
# calls_list = []

# for g in range(0, 1000):
#     numbers_list = random.sample(range(1,76), k=75)
#     call = random.choice(numbers_list)
#     calls_ingame = 1
#     numbers_list.remove(call)
#     crossed_card = cross_num(copy_card, call)
#     is_card_win = check_card(crossed_card)

#     while is_card_win == False:
#         call = random.choice(numbers_list)
#         calls_ingame += 1
#         numbers_list.remove(call)
#         cross_num(crossed_card, call)
#         is_card_win = check_card(crossed_card)
    
#     copy_card = copy.deepcopy(my_bingo_card)
#     calls_list.append(calls_ingame)    

# minimum = min(calls_list)
# maximum = max(calls_list)
# avarage = sum(calls_list)/len(calls_list)

# print(f'The minimum number of calls for the win is: {minimum}')
# print(f'The maximum number of calls for the win is: {maximum}')
# print(f'The avarage number of calls for the win is: {int(avarage)}')

import random
import copy

def check_card_elements(card):
    x = len(card[0])
    y = len(card)
    to_check = [
        [[],[],[],[],[]],
        [[],[],[],[],[]],
        [[],[]]
        ]
    for row in range(x):
        for column in range(y):
            to_check[0][row].append(card[row][column])
            to_check[1][row].append(card[column][row])
           
            if row == column:
                to_check[2][0].append(card[column][row])
                
            if row + column == 4:
                to_check[2][1].append(card[column][row])
    for element in to_check:
        for sub_element in element:
            if sum(sub_element) == 0:
                return True
            
    return False 

def create_bingo_card():
    bingo_card = []
    step = 0
    for letter in range(len('BINGO')):
        bingo_card.append(random.sample(range(1+step, 15+step), k = 5))
        step += 15
    return bingo_card 

def cross_card(card, call_number):
    for line in range(len(card)):
        for number in range(len(card[line])):
            if card[line][number] == call_number:
                card[line][number] = 0
                return card
    return card

def display_card(card):
    x = len(card[0])
    y = len(card)
    to_print = [
        [[],[],[],[],[]],
        [[],[],[],[],[]],
        [[],[],[],[],[]],
        [[],[],[],[],[]],
        [[],[],[],[],[]],
        ]
    for column in range(x):
        for row in range(y):
            to_print[row][column].append(card[column][row])
    
    print(' B  I  N  G  O')
    for line in to_print:
        n1, n2, n3, n4, n5 = line
        line_print = '{:2d} {} {} {} {}'.format(*n1, *n2, *n3, *n4, *n5) 
        print(line_print) 

generated_card = create_bingo_card()
bingo_calls = random.sample(range(1,76), k=75)
calls_list = []

for games in range(0,1000):
    playing_card = copy.deepcopy(generated_card)
    random.shuffle(bingo_calls)
    for numbers in range(len(bingo_calls)):
        n_call = bingo_calls[numbers]
        cross = cross_card(playing_card, n_call)
        check = check_card_elements(cross)
        if check:
            calls_list.append(numbers+1)
            break

minimum = min(calls_list)
maximum = max(calls_list)
avarage = sum(calls_list)//len(calls_list)

display_card(generated_card)
print(f'The minimum number of calls for the win is: {minimum}')
print(f'The maximum number of calls for the win is: {maximum}')
print(f'The avarage number of calls for the win is: {avarage}')

