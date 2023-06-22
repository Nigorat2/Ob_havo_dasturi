# import requests

# url = "https://coronavirus-smartable.p.rapidapi.com/stats/v1/UZ/"

# headers = {
# 	"X-RapidAPI-Key": "0c27596b8fmshc1d099d4db53672p13d675jsncace33cd1463",
# 	"X-RapidAPI-Host": "coronavirus-smartable.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# kassalanganlar_soni = response.json()['stats']['totalConfirmedCases']
# tuzalganlar_soni = response.json()['stats']['totalRecoveredCases']
# vafot_etganlar_soni = response.json()['stats']['totalDeaths']
# print(f"O'zbekistonda COVID19 kassaligi bo'yicha  vafot etganlar soni: {vafot_etganlar_soni}\nTuzalganlar soni:{tuzalganlar_soni}n kasallangallar soni:{kassalanganlar_soni}")


const axios = require('axios');  

const options = {
  method: 'GET',
  url: 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/team',
  params: {name: 'BARCELONA'},
  headers: {
    'X-RapidAPI-Key': '0c27596b8fmshc1d099d4db53672p13d675jsncace33cd1463',
    'X-RapidAPI-Host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com'
  }
};

try {
	const response = await axios.request(options);
	console.log(response.data);
} catch (error) {
	console.error(error);
}


