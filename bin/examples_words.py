from wordnik import *

apiUrl = 'http://api.wordnik.com/v4'
apiKey = '4462dc0720a385afcc3010a95cc0e83ffa65273a6343c3a9c'
client = swagger.ApiClient(apiKey, apiUrl)


wordApi = WordApi.WordApi(client)
word = raw_input("Enter a word to get examples of: ")
example = wordApi.getExamples(word)

print example