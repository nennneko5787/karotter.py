import asyncio

from karotter import Gender, Karotter

karotter = Karotter()


async def main():
    print(await karotter.login("username", "password", Gender.FEMALE))
    print(await karotter.getUserByUserName("karotter"))


if __name__ == "__main__":
    asyncio.run(main())
