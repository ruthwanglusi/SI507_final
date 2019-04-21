from SI507project_tool_app import *

def set_get_type(parkType):
    qType = Type.query.filter_by(name=parkType).first()
    if not qType:
        qType = Type(name=parkType)
        session.add(qType)
        session.commit()
    return qType.id

def set_get_state(eachState):
    qState = State.query.filter_by(name=eachState).first()
    if not qState:
        qState = State(name=eachState)
        session.add(qState)
        session.commit()
    return qState

def new_park(parkName,parkDes,parkType,stateLst):
    if Park.query.filter_by(name=parkName).first():
        pass
    else:
        park = Park(name=parkName, descrip=parkDes,type_id=set_get_type(parkType))

        #append the states (many-many)
        sLst = []
        try:
            for i in stateLst:
                sLst.append(set_get_state(i))
        except:
            print('empty list for states')
            # ??? this doesn't print

        for s in sLst:
            park.states.append(s)
        session.add(park)
        session.commit()

##### Run the Program #####
if __name__ == '__main__':
    pass
