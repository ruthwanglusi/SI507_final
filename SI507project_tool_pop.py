from SI507project_tool_app import *

def set_get_type(parkType):
    print(parkType)
    qType = Type.query.filter_by(name=parkType).first()
    print(qType)
    if not qType:
        qType = Type(name=parkType)
        session.add(qType)
        session.commit()
        tid = qType.id
    return tid

def set_get_state(eachState):
    qState = State.query.filter_by(name=eachState).first()
    if not qState:
        qState = State(name=eachState)
        session.add(qState)
        session.commit()
    return qState

def new_park(name,descrip,type_id,states):
    if Park.query.filter_by(name=parkName).first():
        pass
    else:
        sLst = []
        for i in range(len(stateLst)):
            eachState = stateLst[i]
            sLst.append(set_get_state(eachState))

        park = Park(name=parkName, descrip=parkDes,type_id=tid)
        for s in range(len(sLst)):
            park.states.append(s)
        session.add(park)
        session.commit()

##### Run the Program #####
if __name__ == '__main__':
    pass
