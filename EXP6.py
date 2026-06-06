def vacuum_cleaner():
    rooms = {'A':'Dirty', 'B':'Dirty'}
    location = 'A'

    while 'Dirty' in rooms.values():
        if rooms[location] == 'Dirty':
            print("Cleaning Room", location)
            rooms[location] = 'Clean'
        location = 'B' if location == 'A' else 'A'

    print("All rooms are clean")

vacuum_cleaner()
