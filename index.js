const request = require('request-promise');
const cheerio = require('cheerio');
const fs = require('fs');
const json2csv = require('json2csv').Parser;

let currentPage = null;
const lastPage = 3;
const hasNextPage = () => currentPage < lastPage;

async function getResponse(...header) {
    await request(header);
}

function nextUri() {
    currentPage = currentPage + 1 ?? 1;
    return `https://www.gktoday.in/current-affairs/page/${currentPage}/`;
}

function generateHeader() {
    return {
        uri: nextUri(),
    };
}

(async () => {
    const collection = [];
    
    while (hasNextPage()) {
        const response = getResponse(generateHeader());
        const $ = cheerio.load(response);
        const title = $('h1[id="list"] > a');
        
        for (const node of title) {
            let actualTitle = node.children[0].data;
            collection.push(actualTitle);
        }
        console.log(`data at page ${currentPage} is ${collection}`);
        console.log(collection);
    }

    console.log('data is');
    console.log(collection);
})();
