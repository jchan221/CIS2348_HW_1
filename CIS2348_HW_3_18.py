# Joshua Chan
# 1588459
import math
wall_height = int(input('Enter wall height (feet):''\n'))
wall_width = int(input('Enter wall width (feet):''\n'))
wall_area = wall_height * wall_width
print('Wall area:',wall_area,'square feet')
# The prompts above will record the wall height and width and calculate the area
paint = 350
paint_needed = wall_area / paint
print('Paint needed:','{:.2f}'.format(paint_needed),'gallons')
print('Cans needed:',math.ceil(paint_needed),'can(s)''\n')
# Above will find the amount of paint needed and number of cans necessary
colors = {'red':35,'blue':25,'green':23}
color_choose = input('Choose a color to paint the wall:''\n')
if color_choose == 'red':
    print('Cost of purchasing red paint: $'+str(colors.get('red') * math.ceil(paint_needed)))
if color_choose == 'blue':
    print('Cost of purchasing blue paint: $'+str(colors.get('blue') * math.ceil(paint_needed)))
if color_choose == 'green':
    print('Cost of purchasing green paint: $'+str(colors.get('green') * math.ceil(paint_needed)))
# Depending on the color the different costs will be calculated

