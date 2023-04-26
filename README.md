# Cron Parser

This is a command-line interface(CLI) application that parses a cron string and expands each field to show the times at which it will run.

It consider the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command(does not handle the special time strings such as "@yearly".)

The input is on a single line:

```
*/15 0 1,15 * 1-5 /usr/bin/find
```

Result:

```
minute 0 15 30 45
hour 0
day of month 1 15
month 1 2 3 4 5 6 7 8 9 10 11 12
day of week 1 2 3 4 5
command /usr/bin/find
```

# Getting started
## Compile and run
In order to compile this project you need python3. You can download it from [here](https://www.python.org/downloads/).
### !important note
It is neccessary to add python to PATH.

After donwloading you can open terminal and run following line, where part in "" is input
```
python3 cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find" 
```

# Navigation
cron.py is a class. Comments inside are describing the whole logic.

cron_parser.py is program that describe cron string. Uses function from cron.py

test.py is file with unit test. It is neccessary to test your code by using such technologies
