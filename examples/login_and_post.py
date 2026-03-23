import asyncio

from karotter import Gender, Karotter

karotter = Karotter()


async def main():
    print(await karotter.login("username", "password", Gender.FEMALE))
    print(await karotter.me())
    post = await karotter.createPost("Hello, Karotter.py!")
    print(post)


if __name__ == "__main__":
    asyncio.run(main())
