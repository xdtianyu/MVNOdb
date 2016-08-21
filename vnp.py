#!/bin/env python3
from collections import OrderedDict

province = OrderedDict()
city = OrderedDict()
provider = OrderedDict()

lines = []


class Info:
    number = ""
    province = 0
    city = 0
    provider = 0

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        v = []
        for key in self.__dict__:
            v.append("{value}".format(value=self.__dict__[key]))
        return ' '.join(v)

with open('data.txt') as f:
    for content in f:
        array = content.strip().split(',')
        # print(array)

        pr = array[1].strip()
        ci = array[2].strip()
        pv = array[3].strip()

        if pr not in province:
            province[pr] = len(province)
        if ci not in city:
            city[ci] = len(city)
        if pv not in provider:
            provider[pv] = len(provider)

        info = Info()
        info.number = array[0].strip()
        info.province = province[pr]
        info.city = city[ci]
        info.provider = provider[pv]

        lines.append(info)

print(province)
print(city)
print(provider)
print(lines)
print()

# number

print('''
CREATE TABLE IF NOT EXISTS number (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT UNIQUE,
    province INTEGER,
    city INTEGER,
    provider INTEGER
 );
''')

print("BEGIN;")

for line in lines:
    print("INSERT INTO number (number, province, city, provider) "
          "VALUES (\"{number}\", {province}, {city}, {provider});"
          .format(number=line.number, province=line.province, city=line.city, provider=line.provider))

print("COMMIT;")

# province

print('''
CREATE TABLE IF NOT EXISTS province (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province TEXT UNIQUE,
    province_id INTEGER
 );
''')

print("BEGIN;")

for key, value in province.items():
    print("INSERT INTO province (province, province_id) "
          "VALUES (\"{province}\", {province_id});"
          .format(province=key, province_id=value))

print("COMMIT;")

# city

print('''
CREATE TABLE IF NOT EXISTS city (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT UNIQUE,
    city_id INTEGER
 );
''')

print("BEGIN;")

for key, value in city.items():
    print("INSERT INTO city (city, city_id) "
          "VALUES (\"{city}\", {city_id});"
          .format(city=key, city_id=value))

print("COMMIT;")

# provider

print('''
CREATE TABLE IF NOT EXISTS provider (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider TEXT UNIQUE,
    provider_id INTEGER
 );
''')

print("BEGIN;")

for key, value in provider.items():
    print("INSERT INTO provider (provider, provider_id) "
          "VALUES (\"{provider}\", {provider_id});"
          .format(provider=key, provider_id=value))

print("COMMIT;")




