//Algorithms: Inventory Update
//Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery. 
//Update the current existing inventory item quantities (in arr1). 
//If an item cannot be found, add the new item and quantity into the inventory array. 
//The returned inventory array should be in alphabetical order by item.

function updateInventory(arr1, arr2) {

    var getResultWithElement = (element, accumulator) => {
        if (!accumulator.map(x => x[1]).includes(element[1]))
            accumulator = [...accumulator, element];
        else
            accumulator = accumulator.map(x => x[1] === element[1] ? [x[0] + element[0], x[1]] : x);
        return accumulator;
    };

    const result = arr2.reduce((accumulator, element) => getResultWithElement(element, accumulator), arr1);
    return sortByName(result);
}

function sortByName(array) {
    const keys = array.map(x => x[1]).sort();
    const result = keys.reduce((accumulator, key) => [...accumulator, array.find(x => x[1] == key)], []);
    return result;
}

//previous solution without reducer
function updateInventoryOld(arr1, arr2) {
    var result = arr1;
    arr2.forEach(element => {
        if (!result.map(x => x[1]).includes(element[1]))
            result = [...result, element]
        else
            result = result.map(x => x[1] === element[1] ? [x[0] + element[0], x[1]] : x);
    });
    return sortByNameOld(result);
}

//previous solution without reducer
function sortByNameOld(array) {
    const keys = array.map(x => x[1]).sort();
    var result = [];
    keys.forEach(key => {
        result = [...result, array.find(x => x[1] == key)];
    });
    return result;
}

// Example inventory lists
var curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
];

var newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
];

console.log(updateInventory(curInv, newInv));