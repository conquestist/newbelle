payload = {
"text" :"nigga",
"chat_id": "-5055440298"
}
import requests

req = requests.post("https://api.telegram.org/bot8407894551:AAFo2ITXhTlwE7gjFx8mKO36G5floRC2JRI/sendMessage", json=payload)

