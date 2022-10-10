exports.handler = async (event) => {
  // TODO implement
  console.log(generateMemberId())
  const response = {
    statusCode: 200,
    body: JSON.stringify(generateMemberId()),
  };
  return response;
};

function generateMemberId() {
  //   min = 10000
  //   max = 99999

  var min = Math.ceil(10000);
  var max = Math.floor(99999);
  return Math.floor(Math.random() * (max - min) + min);
}

var htmlTemplate = "<html lang=\"en-US\">\r\n\r\n<head>\r\n  <meta charset=\"UTF-8\">\r\n  <link rel=\"profile\" href=\"https:\/\/gmpg.org\/xfn\/11\">\r\n  <title>Philadelphia Guild of Handweavers &#8211; Philadelphia, PA<\/title>\r\n  <style>\r\n    .wrapper {\r\n      height: 300px;\r\n      display: flex align-items: center;\r\n      justify-content: center;\r\n    }\r\n\r\n    .content {\r\n      height: 300px;\r\n      display: flex;\r\n      align-items: center;\r\n      justify-content: center;\r\n      font-family: \"Prata\", -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\";\r\n    }\r\n  <\/style>\r\n<\/head>\r\n\r\n<body>\r\n  <div class=\"wrapper\">\r\n    <div class=\"content\"> Thanks for beginning registration for the PGHW Holiday Pop up Sale!<br>\r\n      Your Vendor ID number is <\/div>\r\n  <\/div>\r\n<\/body>"