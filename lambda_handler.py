import json
from datetime import date
from datetime import datetime
from web_scraping import WebScraping


def lambda_handler(event, context):
  payload = event
  # Identificador da coleta
  collect_moment = datetime.now().strftime("%d/%m/%Y|%H:%M:%S")
  id_ = payload["name"][:4] + collect_moment

  # Metadados da coleta
  payload["id_owner"] = id_
  payload["collect_date"] = date.today()

  # Coleta de Dados
  url = f"https://www.airbnb.com.br/s/{payload['localizacao']}/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&date_picker_type=calendar&checkin={payload['check_in']}&checkout={payload['check_out']}&source=structured_search_input_header&search_type=filter_change"
  web_scraping = WebScraping(url)
  rooms = web_scraping.pick_all_rooms()
  collect_result = {
    "id_owner": id_,
    "data": rooms}

  # Envio ao DynamoDB do payload -> metadados da coleta
  ###############################

  # Envio ao S3 do collect_result -> resultado da coleta
  ###############################

  return collect_result

if __name__ == "__main__":
  enter = {
    'name': 'Iury',
    'check_in': '2022-06-20',
    'check_out': '2022-06-30',
    'localizacao': 'Fortaleza'
  }

  print(lambda_handler(enter, " "))