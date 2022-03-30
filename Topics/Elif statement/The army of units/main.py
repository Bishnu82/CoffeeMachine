units_number = int(input())
army = [1000, 500, 50, 10, 1]
if units_number >= army[0]:
    print('legion')
else:
    if units_number >= army[1]:
        print('swarm')
    else:
        if units_number >= army[2]:
            print('horde')
        elif units_number >= army[3]:
            print('pack')
        else:
            print('few' if units_number >= army[4] else 'no army')
