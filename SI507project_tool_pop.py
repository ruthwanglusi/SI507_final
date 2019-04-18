from SI507project_tool_app import *
from SI507project_tool_scrape import *

def set_get_type(parkType):
    qType = Type.query.filter_by(name=parkType)
    if not qType:
        qType = Type(name=parkType)
        session.add(qType)
        session.commit()
    return qType


def set_get_state():
    qState = State.query.filter_by(name=)




'''
3.parse the cached data in park_cache.json and put in park_info.db
'''



        # Locations of the site
        try:
            parkLoc = eachPark.h4.text
            # print(parkLoc)

            # States of the the site
            locSplit = parkLoc.split(',')
            stateLst = []

            for s in locSplit:
                if s.startswith('Various States'):
                    stateLst.append(s.split(' ')[-1].strip())
                elif len(s.strip()) == 2:
                    stateLst.append(s.strip())
                else:
                     pass
            print(stateLst)
            # parkState = ', '.join(stateLst)
            # print(parkState)
            # print()
        except Exception as e:
            parkLoc = None
            parkState = None

        row = Park(name=parkName,descrip='parkDes')
        session.add(row)
        session.commit()



##### Run the Program #####
if __name__ == '__main__':
    pass
