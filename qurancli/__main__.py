#!/usr/bin/python

import click
import requests
from prettytable import PrettyTable

@click.group()
def cli():
    "quran-cli gives you the ability to look up pages, Ayahs, and Surahs in the Quran"
    pass


@cli.command('read-surah')
@click.option('--surahnumber', help='Number of Surah', type=int, required=True)
def read_surah(surahnumber):
    "Look up a Surah in the Quran"
    try:
        r = requests.get('http://api.alquran.cloud/v1/surah/{}/en.ahmedraza'.format(surahnumber))
        output = r.json()

        text = output['data']['ayahs']

        for i in text:
            print(i['text'])
            print('--')
    except:
        print("Please enter a number between 1 and 114, as there are only 114 surahs in the Quran.")


@cli.command('read-ayah')
@click.option('--ayahnumber', help='Number of Ayah', type=int, required=True)
def read_ayah(ayahnumber):
    "Look up an Ayah in the Quran"
    try:
        r = requests.get('http://api.alquran.cloud/v1/ayah/{}/en.ahmedraza'.format(ayahnumber))
        output = r.json()

        text = output['data']['text']
        print(text)
    except:
        print("Please enter a number between 1 and 6,236, as there are only 6,236 ayahs in the Quran")

@cli.command('list-surahs')
def list_surahs():
    "List all Surahs in Quran"
    r = requests.get('http://api.alquran.cloud/v1/surah')
    output = r.json()

    text = output['data']

    for i in text:
        t = PrettyTable(['Surah No.', 'Name', 'Arabic Name'])
        t.add_row([i['number'],i['englishNameTranslation'],i['englishName']])
        print(t)

@cli.command('search-quran')
@click.option('--word', help='Word you wish to search for', type=str, required=True)
def search_quran(word):
    "Search all occurences for a word in the Quran"
    try:
        r = requests.get('http://api.alquran.cloud/v1/search/{}/all/en.ahmedraza'.format(word))
        output = r.json()

        for i in output['data']['matches']:
            t = PrettyTable(['Surah (English Name)', 'Surah (Arabic Name)', 'Text'])
            t.add_row([i['surah']['englishName'], i['surah']['englishNameTranslation'], i['text']])
            print(t)
    except:
        print("That is not a valid option.  Please enter a valid word")



if __name__ == '__main__':
    cli()    
