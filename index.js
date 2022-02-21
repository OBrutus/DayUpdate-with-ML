const request = require('request-promise');
const cheerio = require('cheerio');
const fs = require('fs');
const json2csv = require('json2csv').Parser;

const url = 'https://www.gktoday.in/current-affairs/page/2/';

(async () => {
    const collection = [];
    
    const response = await request({
        uri: url,
    });

    const $ = cheerio.load(response);
    const title = $('h1[id="list"] > a');

    for (const node of title) {
        let actualTitle = node.children[0].data;
        collection.push(actualTitle);
    }

    console.log('data is');
    console.log(collection);

    fs.writeFileSync('collection.json', collection);

    const csv = (new json2csv()).parse(collection);
    fs.writeFileSync('collection.csv', csv);
})();
