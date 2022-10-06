exports.handler = async (event) => {
  console.log(generateMemberId())
  const response = {
    statusCode: 200,
    body: JSON.stringify(generateMemberId()),
  };
  return response;
};

function generateMemberId() {
  var min = Math.ceil(10000);
  var max = Math.floor(99999);
  return Math.floor(Math.random() * (max - min) + min);
}

function getPageTemplate() {
  // todo, create an http template using the styling of pghw website
}