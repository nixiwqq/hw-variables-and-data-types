
# ---------------task 1--------

x = int(input('Enter a number:'))
y = int(input('Enter another number:'))
z = int(input('Enter another number:'))

print('summ:', x + y + z)
print('multiplication:', x * y * z)


# ---------------task 2--------

monthly_salary = int(input('зарплата за місяць: '))
loan = int(input('сума місячного платежу за кредитом у банку: '))
arrears = int(input('заборгованість за комунальні послуги: '))

print('сумма, яка залишиться після всіх виплат:', monthly_salary - (loan + arrears))

# ---------------task 3--------

d1 = int(input('Enter a number for first diargonal:'))
d2 = int(input('Enter another number for the second one:'))

print(( d1 * d2) // 2 )