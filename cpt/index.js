const solveCaptcha = require("@hitthemoney/hcaptcha-solver");
const express = require('express');
const app = express();

function solve() {
    return new Promise(async (resolve, reject) => {
        try {
            const token = await solveCaptcha('https://krunker.io', {
                siteKey: "60a46f6a-e214-4aa8-b4df-4386e68dfde4"
            });
            resolve(token);
        } catch(err) {
            resolve(await solve());
        }
    });
}

app.get('/token', async (req, res) => {
    const token = await solve();
    console.log('Token done');
    res.end(token);
});

app.listen(4000);