function getFinalOpenedDoors(numDoors) {
    var doorStates = new Array(numDoors).fill(false);
    for (var modulo = 1; modulo <= numDoors; modulo++) {
        doorStates = toggleDoorStatesFromModulo(doorStates, modulo, numDoors);
        console.log(doorStates)
    }
    return doorStates.map((doorState, index) => doorState ? index + 1 : undefined).filter(index => index);
}

function toggleDoorStatesFromModulo(doorStates, modulo, numDoors)
{
    return doorStates.map((doorState, index) => (index + 1) % modulo === 0 ? !doorState : doorState);
}

const three = getFinalOpenedDoors(4);


