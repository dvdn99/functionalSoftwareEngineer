
def digit_summer(digits):
    if digits <= 0:
        return 0
    return (digits % 10) + digit_summer(digits // 10)
    

print(digit_summer(2347623))
