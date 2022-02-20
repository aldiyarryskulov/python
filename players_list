players_list = [
                {'name':'Stavros','control' : 3, 'pass' : 4, 'shoot':3, 'stamina': 3, 'accel': 4,'position': 'defender'},
                {'name':'Bilal','control' : 3, 'pass' : 4, 'shoot':4, 'stamina': 3, 'accel': 3,'position': 'defender'},
                {'name':'Ghaylen','control' : 3, 'pass' : 4, 'shoot':3, 'stamina': 3, 'accel': 3,'position': 'defender'},
                {'name':'Bahtiyar','control' : 3, 'pass' : 3, 'shoot':3, 'stamina': 3, 'accel': 3,'position': 'defender'},
                {'name':'Nurlan','control' : 5, 'pass' : 4, 'shoot':5, 'stamina': 3, 'accel': 4,'position': 'winger'},
                {'name':'Amr','control' : 4, 'pass' : 4, 'shoot':4, 'stamina': 3, 'accel': 3,'position': 'winger'},
                {'name':'Daulet','control' : 5, 'pass' : 4, 'shoot':4, 'stamina': 5, 'accel': 5,'position': 'winger'},
                {'name':'ilir','control' : 3, 'pass' : 3, 'shoot':3, 'stamina': 3, 'accel': 3,'position': 'winger'},
                {'name':'Dauren','control' : 4, 'pass' : 3, 'shoot':5, 'stamina': 3, 'accel': 3,'position': 'winger'},
                {'name':'Alexandr','control' : 3, 'pass' : 3, 'shoot':2, 'stamina': 2, 'accel': 2,'position': 'winger'},
                {'name':'Omar','control' : 5, 'pass' : 5, 'shoot':5, 'stamina': 5, 'accel': 5,'position': 'forward'},
                {'name':'Ruslan','control' : 5, 'pass' : 4, 'shoot':5, 'stamina': 4, 'accel': 4,'position': 'forward'},
                {'name':'Nurdos','control' : 4, 'pass' : 4, 'shoot':4, 'stamina': 4, 'accel': 4,'position': 'forward'},
                {'name':'Ulan','control' : 4, 'pass' : 4, 'shoot':4, 'stamina': 4, 'accel': 5,'position': 'forward'},
               ]

def defender():
    x = 0
    new_list = {}
    for name in players_list:
        first_name = name['name']
        if players_list[x]['position'] == "defender":
            a = list(players_list[x].values())
            new_list[first_name] = sum(a[1:-1])
            x = x + 1
        else:
            x = x + 1
    return new_list



def winger():
    x = 0
    new_list = {}
    for name in players_list:
        first_name = name['name']
        if players_list[x]['position'] == "winger":
            a = list(players_list[x].values())
            new_list[first_name] = sum(a[1:-1])
            x = x + 1
        else:
            x = x + 1
    return new_list


def forward():
    x = 0
    new_list = {}
    for name in players_list:
        first_name = name['name']
        if players_list[x]['position'] == "forward":
            a = list(players_list[x].values())
            new_list[first_name] = sum(a[1:-1])
            x = x + 1
        else:
            x = x + 1
    return new_list