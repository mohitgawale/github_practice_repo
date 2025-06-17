// let myDate = new Date()
// console.log(myDate);
// console.log(myDate.toString());
// console.log(myDate.toDateString());
// console.log(typeof myDate);

let myCreatedDate = new Date(2024,1,20)
// console.log(myCreatedDate);
// console.log(myCreatedDate.toString());
// console.log(myCreatedDate.toDateString());


 let myTimestamp =  Date.now()

 console.log(myTimestamp)
 console.log(myCreatedDate.getTime());

 console.log(Date.now());

 console.log(Math.floor(Date.now() / 1000));

 console.log(myCreatedDate.toLocaleString('default',{
  weekday : "long",  
 })
 )




