def well_wishes():
    print("hello")
    print("how are you")
well_wishes()
def weather_condition():
    print('the weather is pleasant in:', spring)
    print('the weather is the same in:', autumn)
spring = "autumn"
autumn = spring
weather_condition()
def add (P, Q):
    return P + Q
def subtract (P, Q):
    return P - Q
def multiply (P, Q):
    return P * Q
def divide (P, Q):
    return P / Q
print("pkease select the operation")
print("a. add")
print("b. subtract")
print("c. multiply")
print("d. divide")
choice = input("please enter your choice(a / b / c / d) ")
num_1 = int (input("please enter the first number: "))
num_2 = int(input("please enter the secind number: "))
if choice == 'a':
    print(num_1 "+",num_2, "=",add(num_1, num_2))
elif choice == 'b':
    print(num_1 "-",num_2, "=",subtract(num_1, num_2))
elif choice == 'c':
    print(num_1 "*",num_2, "=",multiply(num_1, num_2))
 elif choice == 'd':
    print(num_1 "/",num_2, "=",divide(num_1, num_2))
 else:
    print("this is an invalid input")