import requests
from datetime import datetime


import requests

url="https://ethereum.blockpi.network/v1/rpc/public"


def getFirstBlockData(date):
    date=datetime.combine(date, datetime.min.time()).timestamp()


    
    response = requests.post(
        url,
        json={
            'jsonrpc': '2.0',
            'method': 'eth_blockNumber',
            'params': [],
            'id': 1
        }
    )

    
    latest_block_number = int(response.json()['result'], 16)
    first_block_number = 0
    last_block_number = latest_block_number

    lo = first_block_number
    hi = latest_block_number

    # binary search to get probable first block
    while (lo <= hi):

        mid = (lo+hi)//2

        response = requests.post(
            url,
            json={
                'jsonrpc': '2.0',
                'method': 'eth_getBlockByNumber',
                'params': [hex(mid), False],
                'id': 1
            }
        )
        result= response.json()['result']
        block_timestamp = int(result['timestamp'], 16)

        
        if block_timestamp < date:
            first_block_number = mid + 1  
            lo = mid + 1
        else:
            hi = mid - 1

    return first_block_number

str_date="2023-06-25"
date=datetime.strptime(str_date,'%Y-%m-%d')

print(getFirstBlockData(date))