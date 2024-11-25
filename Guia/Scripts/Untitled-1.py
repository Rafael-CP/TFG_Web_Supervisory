import asyncio
from asyncua import *

url = "opc.tcp://192.168.0.1:4840/"

async def main():
    async with Client(url=url) as client:
        # Código do programa
        print("Hello World")

if __name__ == "__main__":
    asyncio.run(main())