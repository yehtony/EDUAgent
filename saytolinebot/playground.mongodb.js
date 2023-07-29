/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// Select the database to use.
use('UserAgentLog');

// Insert a few documents into the sales collection.
db.getCollection('historyChatlog').insertMany([
  {
    userId: 0,
    agentId: 0,
    chatlog: [
      {
        role: 'system',
        content:
          '您現在是一位專門為國小三年級學生根據自然科目互動的聊天機器人，您的名字叫做「地球姊姊」。在與小朋友的對話中，您將根據提問內容，和小朋友進行持續的互動。您不可以主動向小朋友說再見，而且非常歡迎小朋友對回答的內容提出問題，您將竭盡所能地回答和解釋，讓小朋友更深入地了解',
      },
    ],
  },
  {
    userId: 0,
    agentId: 0,
    chatlog: [
      {
        role: 'assistant',
        content: '小朋友早安，請問有什麼問題想問呢？',
      },
    ],
  },
  {
    userId: 0,
    agentId: 0,
    chatlog: [
      {
        role: 'user',
        content: '為什麼會下雨？',
      },
    ],
  },
]);
// Run a find command to view items sold on April 4th, 2014.

/*
const salesOnApril4th = db
  .getCollection('sales')
  .find({
    date: { $gte: new Date('2014-04-04'), $lt: new Date('2014-04-05') },
  })
  .count();

// Print a message to the output window.
console.log(`${salesOnApril4th} sales occurred in 2014.`);

// Here we run an aggregation and open a cursor to the results.
// Use '.toArray()' to exhaust the cursor to return the whole result set.
// You can use '.hasNext()/.next()' to iterate through the cursor page by page.
db.getCollection('sales').aggregate([
  // Find all of the sales that occurred in 2014.
  {
    $match: {
      date: { $gte: new Date('2014-01-01'), $lt: new Date('2015-01-01') },
    },
  },
  // Group the total sales for each product.
  {
    $group: {
      _id: '$item',
      totalSaleAmount: { $sum: { $multiply: ['$price', '$quantity'] } },
    },
  },
]);
*/
