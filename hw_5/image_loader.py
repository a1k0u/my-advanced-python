import os
import sys
import aiohttp
import asyncio
import aiofiles

URL = "https://picsum.photos/200"


async def write_image(path: str, content) -> None:
    async with aiofiles.open(path, "wb") as file:
        await file.write(content)


async def download_image():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            return await response.read()


async def get_new_image(path: str):
    image = await download_image()
    await write_image(path, image)


async def main(path: str, amount: int):
    await asyncio.wait(map(get_new_image, [f"{path}/{n}.jpg" for n in range(amount)]))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        exit("Two arguments are requeired..")

    _, path, amount = sys.argv

    if not os.path.isdir(path):
        exit("Directory does not exist..")

    if not amount.isnumeric():
        exit("Second argument has to be integer..")

    asyncio.run(main(path, int(amount)))
