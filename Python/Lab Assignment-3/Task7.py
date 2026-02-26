while True:
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    if start < end:
        break
    print("Start must be less than end. Try again.")

print("Prime numbers are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)