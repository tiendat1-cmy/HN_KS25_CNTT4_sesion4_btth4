max_attemps = 5
correct_number = 69
status = False

for i in range(1, 6, 1):
    input_number =  int(input('Mời nhập vào số cần đoán: '))
    if input_number > correct_number: 
        print('Gợi ý: Số của bạn lớn hơn số may mắn ')
    elif (input_number < correct_number):
        print('Gợi ý: Số của bạn nhỏ hơn số may mắn')
    else: 
        status = True
        print('Chúc mừng bạn đã đoán chính xác số may mắn!!')
        break

if status == False:
    print('Bạn đã hết lượt')

print('Trò chơi kết thúc')

    