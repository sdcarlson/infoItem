#!/usr/bin/python
import time
import requests
import base64
from concurrent import futures
import sys


def makeRequest(itemId):
    idBytes = itemId.encode('ascii')
    b64Bytes = base64.b64encode(idBytes)
    b64String = b64Bytes.decode('ascii')
    r = requests.get("https://challenges.qluv.io/items/" +
                     itemId, headers={'Authorization': b64String})
    return r.text


def main():
    if len(sys.argv) < 2:
        print("Usage: infoItem.py <fileName.txt>")
        return
    fileName = sys.argv[1]
    idDict = {}
    with open(fileName, 'r') as f:
        for line in f:
            itemId = line.strip()
            if itemId not in idDict.keys():
                idDict[itemId] = True

    start = time.time()

    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        futureToItem = dict(
            (executor.submit(makeRequest, itemId), itemId) for itemId in idDict.keys())
        for future in futures.as_completed(futureToItem):
            itemId = futureToItem[future]
            try:
                data = future.result()
                print(itemId, data)
            except Exception as exc:
                print('%r generated an exception: %s' % (itemId, exc))

        end = time.time()
        print("The average time per request was   " +
              str((end - start) / len(idDict.keys())) + " seconds")


main()
