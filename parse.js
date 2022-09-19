const puppeteer = require('puppeteer');
const { scrollPageToBottom } = require('puppeteer-autoscroll-down')
const fs = require('fs');

(async function() {
    const link = 'https://vk.com/album-183079258_00';
    
    try {
        const browser = await puppeteer.launch({
            headless: false,
            slowMo: 100,
            devtools: true,
        });

        const page = await browser.newPage();

        await page.setDefaultNavigationTimeout(0);
        await page.goto(`${link}`);

        const lastPosition = await scrollPageToBottom(page, {
            size: 500,
            delay: 250
        })

        const html = await page.evaluate(async () => {
            const data = [];

            try {
                const photosContainer = document.querySelectorAll('.photos_container div a');

                photosContainer.forEach((elem, i) => {
                    const link = elem.href;

                    data.push({
                        id: i,
                        meme: (new URL(link).pathname + '/album-183079258_00/rev').slice(1)
                    })
                })

            } catch (e) {
                console.log(e);
            }

            return data;
        })

        await browser.close();

        console.log(html)

        fs.writeFile('data.json', JSON.stringify(html), (err) => {
            if (err) console.log(err);
        })
    } catch (e) {
        console.log(e);

        await browser.close();
    }
})();