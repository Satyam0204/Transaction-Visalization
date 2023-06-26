from datetime  import datetime,date

import requests

url="https://ethereum.blockpi.network/v1/rpc/public"


def getLatestBlockNumber():
    config={
            "jsonrpc": "2.0",
            "method": "eth_blockNumber",
            "params": [],
            "id": 1
        }
    
    response= requests.post(url,json=config)
    blocknumber=response.json()['result']
    return int(blocknumber,16)

def getBlockData(blocknumber):
    config={
                "jsonrpc": "2.0",
                "method": "eth_getBlockByNumber",
                "params": [hex(blocknumber), False],
                "id": 1
            }

    response=requests.post(url,json=config)
    block_data=response.json()['result']
    
    
    
    block_timestamp = int(block_data["timestamp"], 16)
    # block_date = datetime.fromtimestamp(block_timestamp)
    # print(block_timestamp)
    # print({"block_date":block_date})
    # print({"block_date":block_date,"block_number":hex(blocknumber)})
    print(block_data)

def getspecificblocknumber(date):
    blocknumber=getLatestBlockNumber()

    while(blocknumber>0):
        
        block_date=datetime.fromtimestamp(getBlockData(blocknumber))
        # print(block_date)
        if block_date==date:

            print({"block_date":block_date,"block_number":hex(blocknumber)})

            break
        else:
            blocknumber-7104

    return blocknumber

# getBlockData(getLatestBlockNumber())
# print(hex(getLatestBlockNumber()))
# inputdate=datetime(2023,6,25).date()
# getspecificblocknumber(inputdate)