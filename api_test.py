import requests
import json


def main():
        print('This test program represents usage of Alpha Vantage API\n'
              'and returns you a JSON file with info about leaps and volume\n'
              'aka quantity of operations on shares of the given company\n''
              'in certain period\n\n')
        company = input('Enter company name:')
        function = 'TIME_SERIES_' + input('Category of information you need INTRADAY/DAILY/WEEKLY/MONTHLY:')

        if function == 'TIME_SERIES_INTRADAY':
                interval = input('Enter time interval 1/5/15/30/60 mins:') + 'min'
        else:
                interval = None

        if function == 'TIME_SERIES_DAILY':
                outputsize = input('If you want to get recent data: type \'compact\'\nIf you want to get data '
                                   'for the past 20 years: type \'full\':\n')
        else:
                outputsize = None

        print(parse_data(get_data(function, company, interval, outputsize)))


def get_data(function, symbol, interval, outputsize):
        data = {"function": function,
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize,
        "datatype": "json",
        "apikey": "YGGL6LXB7FIUYNWF"}
        response = requests.get("https://www.alphavantage.co/query", data)
        data = response.json()
        return data


def parse_data(data):
        parsed_data = dict()
        keys = data.keys()
        for each in keys:
                if each != 'Meta Data':
                        keyword = each
        for time in data[keyword]:
                parsed_data[time] = dict()
                parsed_data[time]['leap'] = float(data[keyword][time]['1. open']) - float(data[keyword][time]['4. close'])
                parsed_data[time]['volume'] = data[keyword][time]['5. volume']
        return parsed_data


def return_json(parsed_data):
        with open('test.json', 'w') as json_file:
            json.dumps(parsed_data, json_file)


if __name__ == '__main__':
    main()

