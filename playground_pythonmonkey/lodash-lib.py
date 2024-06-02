import pythonmonkey as pm

if __name__ == "__main__":
    lodash = pm.require("../javascript/lodash-lib.js")
    composed = lodash.flow(
        lambda x: x * x,
        lambda x: x + 10,
    )
    print(composed(2))
