import pythonmonkey as pm
import asyncio

if __name__ == "__main__":
    fxts = pm.require("../javascript/fxts-lib.js")
    print(dir(fxts))

    async def async_fn():
        result = await fxts.fxts.pipe(
            [1, 2, 3, 4],
            fxts.asyncAdd,
        )
        print(f"Result is - {result}")

    asyncio.run(async_fn())
