var search1= 'googel'
var store = require('app-store-scraper');
var s= store.search({
  term: search1,
  num: 10,
  page: 1,
  country : 'us',
  lang: 'lang'
})
.then(console.log)
.catch(console.log);



