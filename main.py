codes = '98 98 217'

if len(codes) > 0:
    colors = {'red' : codes.split(' ')[0], 'green' : codes.split(' ')[1], 'blue' : codes.split(' ')[2]}
    print('red: ' + str(colors['red']))
    print('green: ' + str(colors['green']))
    print('blue: ' + str(colors['blue']))
    print('max: ' + max(colors, key=colors.get))

  
    if int(colors['red']) + int(colors['green']) + int(colors['blue']) == 0:
            print('black')
    elif int(colors['red']) + int(colors['blue']) + int(colors['green']) == int(colors['red']) * 3:
            print('white')

    if colors['red'] == colors['blue']:
        if colors['green'] > colors['red']:
            print('green')
        else:
            print('magenta')

    if colors['red'] == colors['green']:
        if colors['blue'] > colors['red']:
            print('blue')
        else:
            print('yellow')
            
    if colors['blue'] == colors['green']:
        if colors['red'] > colors['blue']:
            print('red')
        else:
            print('cyan')
            
    elif colors['red'] != colors['green']:
        if colors['green'] != colors['blue']:
            print(max(colors, key=colors.get))
            
    else:
        print('black')
