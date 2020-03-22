
//1st implementation

function sym() {
  
    if (arguments.length === 0)
        return [];

    if (arguments.length === 1)
        return arguments[0];

    if (arguments.length === 2)
        return twoElementsSym(arguments[0], arguments[1]);

    const [firstArray, secondArray, ...nextArrays] = arguments;
    return sym(twoElementsSym(firstArray, secondArray), ...nextArrays);


    function twoElementsSym(firstArray, secondArray)
    {
        return [...twoElementsSymOneSide(firstArray, secondArray), ...twoElementsSymOneSide(secondArray, firstArray)];
    }

    function twoElementsSymOneSide(firstArray, secondArray)
    {
        var result = [];

        firstArray.forEach(element => {
            if (!secondArray.includes(element) && !result.includes(element))
                result.push(element);  
        });

    return result;
    }
}

console.log(sym([1, 2, 5], [2, 3, 5], [3, 4, 5]));
console.log(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]));



//2nd implementation, using a reducer and spreaded args object as arguments is an array like object

const symWithReducer = (...args) => [...args].reduce(symReducer)

const symReducer = (accumulatedArray, currentArray) => {

    var result = [];

    accumulatedArray.forEach(element => {
        if (!currentArray.includes(element) && !result.includes(element))
            result.push(element);
    });
    currentArray.forEach(element => {
        if (!accumulatedArray.includes(element) && !result.includes(element))
            result.push(element);
    });


    return result;
}


console.log(symWithReducer([1, 2, 5], [2, 3, 5], [3, 4, 5]));
console.log(symWithReducer([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]));


