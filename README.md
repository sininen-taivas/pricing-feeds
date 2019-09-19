# Ergo-token price
## Installation
Just install python of 3rd version.

## currency Script
Retrieves price ergo-token in fiat currency
### Usage
```bash
python3 currency.py [short-code of currency]
```

### Command Line Options
- `-h`, `--help`- show this help message and exit

### How it works
- receives short currency code (eur by example)
- default is usd
- makes an api request, parses and print to console the current price of ergo-token

## gold Script
Retrieves price of gold
### Usage
```bash
python3 gold.py [api-key]
```

### Command Line Options
- `-h`, `--help`- show this help message and exit
api-key - unique API-key received on www.quandl.com

### How it works
- receives api-key as required params
- makes an api request, parses and print to console the last price of gold
