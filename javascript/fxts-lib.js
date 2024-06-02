const fxts = require('@fxts/core');

function asyncAdd(numbers) {
    return new Promise((resolve) => {
        setTimeout(() => resolve(numbers.map((number) => number + 100000)), 3000);
    });
}

exports.fxts = fxts;
exports.asyncAdd = asyncAdd;
