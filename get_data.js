var fetch=require('node-fetch');
var fs=require('fs');
(async ()=>{
  let user_list=[];
  for(page=101;page<=150;page++){
    var list=await (await fetch("https://www.codechef.com/api/ratings/all?sortBy=global_rank&order=asc&page="+page+"&itemsPerPage=40", {
      "headers": {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "sec-ch-ua": "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-csrf-token": "a5253db7593af11f4bdcbfa2f5fbf59905a99c22c9fe20a9b80f908c9d25a4b0",
        "x-requested-with": "XMLHttpRequest",
        "cookie": "_gcl_au=1.1.601643350.1616615406; _ga=GA1.2.1096063667.1616615406; _gid=GA1.2.1606896325.1616615406; _fbp=fb.1.1616615867732.258913079; __utmc=100380940; __utmz=100380940.1616616724.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __auc=f16b257417865dd952ae1ab35a7; _clck=1ngnqic; SESS93b6022d778ee317bf48f7dbffe03173=60c9e72b826b8cdf622e605cc51dc430; __utma=100380940.1096063667.1616615406.1616620250.1616623447.3; __utmt=1; __utmb=100380940.2.10.1616623447"
      },
    "referrer": "https://www.codechef.com/ratings/all?itemsPerPage=40&order=asc&page="+(page==1?2:(page-1))+"&sortBy=global_rank",
    "referrerPolicy": "strict-origin-when-cross-origin",
    "body": null,
    "method": "GET",
    "mode": "cors"
  })).json();
  console.dir(page)
  fs.writeFileSync("result."+page+".json",JSON.stringify(list))
  user_list=user_list.concat(list.list)
}
})();


// fetch("https://www.codechef.com/api/ratings/all?sortBy=global_rank&order=asc&page=1&itemsPerPage=20", {
//   "headers": {
//     "accept": "application/json, text/javascript, */*; q=0.01",
//     "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
//     "if-modified-since": "Thu, 25 Mar 2021 18:26:49 +0000",
//     "sec-ch-ua": "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
//     "sec-ch-ua-mobile": "?0",
//     "sec-fetch-dest": "empty",
//     "sec-fetch-mode": "cors",
//     "sec-fetch-site": "same-origin",
//     "x-csrf-token": "461450a4dfe53fb06d087cc331f2e5704fcad9cc33780cc6daf0689f1b7af042",
//     "x-requested-with": "XMLHttpRequest",
//     "cookie": "__utma=100380940.2080889437.1616696792.1616696792.1616696792.1; __utmc=100380940; __utmz=100380940.1616696792.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; _gcl_au=1.1.1609521839.1616696792; _fbp=fb.1.1616696792499.251559443; _ga=GA1.2.2080889437.1616696792; _gid=GA1.2.529374137.1616696793; _gat_UA-141612136-1=1; _clck=1yy6gd1; SESS93b6022d778ee317bf48f7dbffe03173=a5fc1062508437bed95f7279f910c6df; userkey=371aa6f1b87783a68c6cbb9758291572; ide=not-ide; i-love-cookies=yes; __utmb=100380940.3.10.1616696792"
//   },
//   "referrer": "https://www.codechef.com/ratings/all",
//   "referrerPolicy": "strict-origin-when-cross-origin",
//   "body": null,
//   "method": "GET",
//   "mode": "cors"
// });