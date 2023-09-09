# ChuenApp
## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation
1. After downloading ``ChuenApp-2.0.1.zip``, extract the file.
2. Click ``ChuenApp-2.0.1/ChuenApp-2.0.1`` then find the ``ChuenApp.exe``.
3. The system may show a blue screen stopping you from open the file, but just click ``More Info`` then ``Run Anyway`` to continue.

## Usage
- When open the app, it will show ``Enter a command: ``
- Type ``/calculator`` to run a calculator
- Type ``/clock`` to run a calculator
- Type ``/install`` to install other apps: ``dice``, ``wordle``
- In any app, type ``/exit`` to exit the app

## Features
### Calculator
- When typing ``/calculator``, the app will show ``(+/-/x/÷): ``
- Type ``+/-/x/÷`` to add, subtract, multiply or divide
- The app will show ``Number 1:`` then ``Number 2:``, type the numbers to calculate
### Clock
- When typing ``/clock`` the app will show:
  ```
  It's currently <time>.
  Enter a command:
  ```
- Type ``/time`` to show your local time again
- When typing ``/timezone``, the app will show ``Enter timezone: ``, type a timezone to continue. e.g. Asia/Tokyo
- Check the timezone list at [here](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568)
- When typing ``/timer``, the app will show ``Counts from (seconds): ``, enter a duration then the app will respond when the time is over
### Dice
- To use dice, install dice by using ``/install``
- After installing, when typing ``/dice``, the app will show ``Enter dice range:from 1 to ``, enter the range and the app will give you a random number
### Wordle
- In each game, you have 6 attempts to guess a random word
- When the word contains a letter in your guess but is in the wrong place, the feedback will show ``O``
- When the word contains a letter in your guess and is in the correct place, the feedback will show ``X``
- Other letters will be shown as ``_``
- To give up, type ``/give up``

