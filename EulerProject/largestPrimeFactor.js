function largestPrimeFactor(number) {
    var rest = number;
    var i = 2;
    while(i < rest)
    {
      if (rest % i === 0) {
        rest = rest / i;
      }
      else {
        i = i+1;
      }
    }
    return rest;
  }
  
  var factor = largestPrimeFactor(13195);