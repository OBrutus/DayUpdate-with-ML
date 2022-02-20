const request = require('request-promise');
const cheerio = require('cheerio');
const fs = require('fs');
const json2csv = require('json2csv').Parser;

const movie = 'https://www.imdb.com/title/tt1877830/?ref_=nv_sr_srsg_0';

(async () => {
    const imdb_data = [];
    
    const response = await request({
        uri: movie,
        headers: {
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,hi;q=0.8'
        },
        gzip: true
    });

    console.log(response);
    fs.writeFileSync('index.html', response);
    const $ = cheerio.load(response);
    const title = $('div[class="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt"] > h1').innerText;
    const rating = $('div[class="TrendingButton__TrendingScore-sc-bb3vt8-1 efbXIW"]').innerText;
    const summary = $('span[class="GenresAndPlot__TextContainerBreakpointXS_TO_M-sc-cum89p-0 kHlJyu"]').innerText;

    imdb_data.push({ title, rating, summary });
    console.log(imdb_data);

    const csv = (new json2csv()).parse(imdb_data);
    fs.writeFileSync('imdb_data.csv', csv);
})();
