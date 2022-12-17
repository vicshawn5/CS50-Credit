def Luhn(number):

    CardLen = len(str(number))
    if (CardLen != 13 and CardLen != 15 and CardLen != 16):
        print("INVALID")

    else:
        #Loop to multiply every other number, starting from the second to last, by 2
        num = number
        sum = 0
        while num > 0:
            digit = num % 100
            num = num // 100
            digit = digit // 10
            multi = digit * 2
            s_multi = str(multi)
            #Loop to add each digit up after the multiplication
            for n_digit in s_multi:
                sum = sum + int(n_digit)

        #Loop to add the numbers not multiplied by 2
        num = number
        sum_2 = 0
        while num > 0:
            digit_2 = num % 10
            num = num // 100
            s_add = str(digit_2)
            for n_digit_2 in s_add:
                sum_2 = sum_2 + int(n_digit_2)

        total_sum = sum + sum_2

        Number = str(number)
        #print if length of number isn't 13, 14 or 16, and if the last digit of the total sum isn't 0
        if total_sum % 10 != 0:
            print("INVALID")

        #print card provider if the last digit of the total sum is 0
        elif total_sum % 10 == 0:
            if CardLen == 15 and int(Number[0]) == 3 and (int(Number[1]) == 4 or 7):
                print("AMEX")
            if (CardLen == 13 or 16) and (int(Number[0]) == 4):
                print("VISA")
            elif CardLen == 16 and int(Number[0]) == 5 and (int(Number[1]) == 1 or 2 or 3 or 4 or 5):
                print("MASTERCARD")

number = int(input("Card Number: "))
Luhn(number)

