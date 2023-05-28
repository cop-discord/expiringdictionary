import asyncio,datetime,time
from typing import Any

class ExpiringDictionary(object):
    def __init__(self):
        self.dict={}
        self.rl={}

    async def set(self,key:str,value:Any,expiration:int=60):
        self.dict[key]=value
        await asyncio.sleep(expiration)
        if key in self.dict:
            self.dict.pop(key)

    async def delete(self,key:str,value:Any):
        if key in self.dict:
            return 1
        else:
            return 0

    async def get(self,key:str):
        if key in self.dict:
            return self.dict[key]
        else:
            return 0

    async def keys(self):
        return list(self.dict.keys())

    async def ratelimit(self,key:str,amount:int,bucket:int=60):
        if key not in self.dict:
            self.dict[key]=1
            self.rl[key]=amount
            yield False
            await asyncio.sleep(bucket)
            if key in self.dict:
                self.dict.pop(key)
                self.rl.pop(key)
        else:
            try:
                self.dict[key]+=1
                if self.dict[key] >= self.rl[key]:
                    return True
                else:
                    return False
            except:
                return await self.ratelimit(key,amount,bucket)
