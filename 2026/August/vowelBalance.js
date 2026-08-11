/*
Vowel Balance

Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

    The string can contain any characters.
    The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
    If there's an odd number of characters in the string, ignore the center character.


*/


function isBalanced(s) {
  //as in condition, if length of string is odd, ignore the middle character
  const firstHalf = s.length%2==0 ? s.slice(0,s.length/2) : s.slice(0,Math.floor(s.length/2));
  const secondHalf = s.length%2==0 ? s.slice(s.length/2, s.length) : s.slice(Math.ceil(s.length/2), s.length);
  
  const vowels = "aeiou";
  let firstHalfCount = 0;
  let secondHalfCount = 0;


  for (let m of firstHalf.toLowerCase()){firstHalfCount += 1 ? vowels.includes(m) : firstHalfCount+=0};
  for (let n of secondHalf.toLowerCase()){secondHalfCount += 1 ? vowels.includes(n) : secondHalfCount+=0};
  
 if (firstHalfCount == secondHalfCount){return true;}
 else {return false;};
}

console.log(isBalanced("racecar"))
