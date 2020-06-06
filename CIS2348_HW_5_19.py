# Joshua Chan
# 1588459
services = {'oil change':35,'tire rotation':19,'car wash':7,'car wax':12}
print('Davy\'s auto shop services')
print('Oil change -- $'+str(services.get('oil change')))
print('Tire rotation -- $'+str(services.get('tire rotation')))
print('Car wash -- $'+str(services.get('car wash')))
print('Car wax -- $'+str(services.get('car wax')))
# The output above will create the menu for the user to choose services
service_1 = input('\n''Select first service:''\n')
service_2 = input('Select second service:''\n')
print('\n''Davy\'s auto shop invoice''\n')
# The prompts above will allow the user to choose the services they want
service_1_value = 0
service_2_value = 0
if service_1 == 'Oil change':
    service_1_value = services.get('oil change')
    print('Service 1: Oil change, $'+str(service_1_value))
if service_1 == 'Tire rotation':
    service_1_value = services.get('tire rotation')
    print('Service 1: Tire rotation, $'+str(service_1_value))
if service_1 == 'Car wash':
    service_1_value = services.get('car wash')
    print('Service 1: Car wash, $'+str(service_1_value))
if service_1 == 'Car wax':
    service_1_value = services.get('car wax')
    print('Service 1: Car wax, $'+str(service_1_value))
if service_1 == '-':
    print('Service 1: No service')
# The if statements above will access the dictionary and set the appropriate values to the user's input
if service_2 == 'Oil change':
    service_2_value = services.get('oil change')
    print('Service 2: Oil change, $'+str(service_2_value))
if service_2 == 'Tire rotation':
    service_2_value = services.get('tire rotation')
    print('Service 2: Tire rotation, $'+str(service_2_value))
if service_2 == 'Car wash':
    service_2_value = services.get('car wash')
    print('Service 2: Car wash, $'+str(service_2_value))
if service_2 == 'Car wax':
    service_2_value = services.get('car wax')
    print('Service 2: Car wax, $'+str(service_2_value))
if service_2 == '-':
    print('Service 2: No service')
# The if statements above will reflect the price of the service chosen by the user for service 2
total = service_1_value + service_2_value
print('\n''Total: $'+str(total))
# Above will add the price of the two services together and show the user
