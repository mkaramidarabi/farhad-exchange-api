const crypto = require('crypto');
const secret = '87ClgUfZ3OfSSpsb';

const hash = crypto.createHmac('sha256', secret)
                   // updating data
                   .update('BTC_USDT:0')
                   // Encoding to be used
                   .digest('hex');
console.log(hash);