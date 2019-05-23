const fs = require('fs');

function readCsv(filename) {
    return fs.readFileSync(filename, 'utf-8');
}

// BEGINNING OF PART 1

// BUILD DICTIONARY FOR ALL SITES VISITED BY ALL USERS
var sheet =  readCsv('input2.csv');
var arrayRows = sheet.split('\n');
var custPageDict = {};
var custNum;
var visitedPage;

for (i = 0; i < arrayRows.length-1; i++){
  custNum = arrayRows[i].split(',')[1];
  visitedPage = arrayRows[i].split(',')[2];
  if (custPageDict[custNum]){
    custPageDict[custNum] += visitedPage;
  }
  else {
    custPageDict[custNum] = visitedPage;
    //otherwise first element will be undefined.
  }
}

// BUILD DICTIONARY FOR ALL OCCURANCES OF DIFFERENT PAGE PATH AND THEIR OCCURANCE COUNT
var pathFreqDict = {};

for (var cust in custPageDict){
  var arraySites = custPageDict[cust].trim().split(' ');
  while (arraySites.length > 2){
    var threePath = arraySites.slice(0,3).join();
    if (pathFreqDict[threePath]){
      pathFreqDict[threePath] += 1;
    }
    else {
      pathFreqDict[threePath] = 1;
    }
    arraySites.shift();
  }
}

// FIND MOST COMMON PATH AND THE TIME IT APPEARED
var mostFreqCount = 0;
var mostFreqPath = ''

for (var path in pathFreqDict){
  var freq = pathFreqDict[path];
  if (freq > mostFreqCount){
      mostFreqPath = path;
      mostFreqCount = freq;
  }
  else if (freq == mostFreqCount){
      mostFreqPath += " and " + path;
  }
}

// Part 1 answer
console.log("The most common 3 page path(es) is/are [%s], which was/were visited %s times.", mostFreqPath, mostFreqCount,)

// END OF PART 1



//BEGINNING OF PART 2

// BUILD DICTIONARY FOR ALL OCCURANCES OF DIFFERENT CUSTUMER VISITS AND SPEED
var custSpeedDict = {};
var pageSpeed;

for (i = 0; i < arrayRows.length-1; i++){
  custNum = arrayRows[i].split(',')[1];
  pageSpeed = arrayRows[i].split(',')[3];
  if (custSpeedDict[custNum]){
    custSpeedDict[custNum] += pageSpeed;
  }
  else {
    custSpeedDict[custNum] = pageSpeed;
  }
}

var pathSpeedDict = {};
var pathCustDict = {};

// SINCE ENTRIES IN THIS DICTIONARY IS ONE TO ONE WITH PREVIOUSLY MADE DICTIONARY, COMBINE THE TWO TO MAKE A NEW DICTIONARY FOR PATH TO SPEED RELATIONASHIP
for (var cust in custSpeedDict){
  var arraySpeeds = custSpeedDict[cust].trim().split(' ');
  var arraySites = custPageDict[cust].trim().split(' ');
  while (arraySpeeds.length > 2){
    var totalSpeed = 0;
    for (var i = 0; i < 3; i++) {
      totalSpeed += parseFloat(arraySpeeds[i]);
    }
    var threePath = arraySites.slice(0,3).join();
    if (pathSpeedDict[threePath]){
      pathSpeedDict[threePath] += " " + totalSpeed;
      pathCustDict[threePath] += " " + cust.trim();
    }
    else {
      pathSpeedDict[threePath] = totalSpeed;
      pathCustDict[threePath] = cust.trim();
    }
    arraySites.shift();
    arraySpeeds.shift();
  }
}

// FIND SLOWEST PATH AND THE TIME IT TOOK AND AFFECTED USERS
var slowestPathTime = 0;
var slowestPath = ''
var affectUser = ''

var speeds = '';
for (var path in pathSpeedDict){
    var speeds = pathSpeedDict[path]+'';
    speeds = speeds.split(' ');
  for (var i in speeds){
    if (parseInt(speeds[i]) > slowestPathTime){
        slowestPath = path;
        slowestPathTime = speeds[i];
        affectUser = pathCustDict[path].split(' ')[i];
    }
    else if (parseInt(speeds[i]) == slowestPathTime){
        slowestPath += " and " + path;
        affectUser += " and " + pathCustDict[path].split(' ')[i];
    }
  }
}

// Part 2 answer
console.log("The slowest 3-page path is/are %s at %s, the user impacted was/were %s", slowestPath, slowestPathTime, affectUser)

// END OF PART 2
