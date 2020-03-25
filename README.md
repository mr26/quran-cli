# quran-cli
quran-cli gives you the ability to read Ayahs and Surahs within the Quran, as well as search for text.

# Installation
- Clone the repo ```git clone https://github.com/mr26/quran-cli.git```
- Then run the install script: ```qurancli/install.sh```

# Usage

Examples:

```[root@desktop ~]# quran-cli --help
Usage: quran-cli [OPTIONS] COMMAND [ARGS]...

  quran-cli gives you the ability to look up pages, Ayahs, and Surahs in the
  Quran

Options:
  --help  Show this message and exit.

Commands:
  list-surahs   List all Surahs in Quran
  read-ayah     Look up an Ayah in the Quran
  read-surah    Look up a Surah in the Quran
  search-quran  Search all occurences for a word in the Quran
  
  ```

```quran-cli list-surahs```


```quran-cli read-surah --surahnumber 10```



