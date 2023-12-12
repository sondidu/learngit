# I've found this problem from blackpenredpen
# https://youtu.be/zdAJXil-NvA?si=1C_9gyToUY-GohCt
# Yeah, imma try to bruteforce it.


# x + y = 8
# what is the max of x^y
x = 3.0

ans = 0
i = 0
while x < 4.5:
    y = 8 - x
    x_power_y = x ** y
    print(f'i: {i}, x: {x}, y: {y}, x^y: {x_power_y}')
    ans = max(ans, x_power_y)
    x += 0.01
    i += 1

print()
print(f'ans: {ans}')