(Please forgive me the lack of proper terminology, structure etc.)<br>
**This project is heavily WIP and everything is subject to change**

# Design notes:
The language is supposed to reflect the nature of the species.<br>
This means that the sentences should be short and
contain as much information as possible, as Doguns speak slowly. <br>
I am also trying to make the language simple. I try to look at every feature and question why does it exist.

# Phonetics:
## Pronunciation:
For more information on pronunciation [click on this table](https://www.internationalphoneticalphabet.org/ipa-sounds/ipa-chart-with-sounds/).
### Vowels:
|       | near-front    | back                   |
|:-----:|:-------------:|:----------------------:|
| close | i /I/ ii /I:/ | u /u/                  |
| mid   | e /ɛ/ ee /ɛ:/ | o /o/<br>a /ʌ/ aa /ʌ:/ |

### Consonants
|                         | bilabial    | labio-dental | alveolar    | velar       | glottal |
|:-----------------------:|:-----------:|:------------:|:-----------:|:-----------:|:--------|
| plosive                 | p /p/ b /b/ |              | t /t/ d /d/ | k /k/ g /g/ |         |
| nasal                   | m /m/       |              | n /n/       |             |         |
| trill                   |             |              | r /r/       |             |         |
| fricative               |             | f /f/ v /v/  | s /s/       |             | h /ɦ/   |
| lateral<br> approximant |             |              | l /l/       |             |         |

Unused letters: c, j, q, w, y, z<br>
Letter categories:
* Vowels
* Plosives
* Fricatives
* Others

# Grammar (I think?):
## Nouns:
Plural:

|              |  plural | plural<br>collective |
|--------------|:-------:|:--------------------:|
| **postfix**  | a       | e                    |
| **examples** | ------- | -------------------- |
| earth        | earha   | earhe                |
- plural collective = e.g. races, species
  - Dogun as species, not as a group (like a village)
TODO: is "Dohearh" a species or a member of the species?

## Verbs:
- end with "h"
- structure is {tense}-{verb}{pronoun without "d"}
  - (e.g. "I write" =  en- + wroth + a = en-wrotha) ("en" signalises present simple)
- negation is done by adding "n" before pronoun
  - (e.g. "I don't write" = "n" + en- + vroth + a = nen-vrotha)

### tenses
- postfix

| tense              | prefix |
|--------------------|:------:|
| present simple     | en     |
| present continuous | in     |
| past simple        | em     |
| future simple      | ef     |
| imperative         | ---    |
| conditional        | ---    |


TODO: Decide whether to use grammatical aspect to repalce extra tenses
## Pronouns:
|                  | singular | plural      | plural<br>collective|
|------------------|:--------:|:-----------:|:-------------------:|
| 1st person (me)  | da       | daa/<br>dae | dai                 |
| 2nd person (you) | de       | dea         | dei                 |
| 3nd person       | du       | doa         | doi                 |
- 1st person plural:
  - whether the recipient of the speech/text is included
  - Example: friend tells you "We won the lottery!"
    - \+listener = you won too
    - \-listener = you didn't win

possessive pronouns have the prefix "-a" (my = ada)
<br>TODO: Possessive for other words
- either a pre/suf- fix, or something "of" someone

## Prepositions:
## Adverbs:
## Adjectives:
TODO: Possible reserved last leeter (like verbs have)
- absolute: nothing
- comparative: postfix -o
- superlative: postfix -i
## Determiners:
## Conjunctions:
## Interjections:

## Word sructure
One possibility:
- words should start with one of these letters: t, d, k, g, p, b
# Sentence structure:
Same as english for now

# Vocabulary:
| english      | dogun-ish             |
|--------------|-----------------------|
| Dogun        | Dohearh (living earth)|
| being (noun) | baen                  |
| earth        | earh                  |
| fire         | firae                 |
| friend       | frod                  |
| letter       | lotod                 |
| stone        | stod                  |
| wynnic       | wynnic                |
|---------|-----------|
| speak   | spoh      |
| write   | vroth     |
| live    | doh       |
| welcome | volcoh    |
| be      | dah       |
| speak   | spoh      |
|---------|-----------|
| on      | ho        |
| to      | to        |
| and     | o         |
| from    | fo        |


# Writing system:
## Alphabet:
Each column represents an iteration. First iteration is in the style of already existing letters used for ceremonial purposes, the fourth one is simplified for use in common writing.<br>
TODO: image styling + Vowel rename<br>
![](images/DogunVowelDraft1.png)
![](images/DogunPlosivesDraft1.png)
![](images/DogunFricativesDraft1.png)
![](images/DogunOthersDraft1.png)

# Examples:
| english                            | dogun-ish                      |
|------------------------------------|--------------------------------|
| I write                            | en-vrotha                      |
| He speaks                          | en-spohu                       |
| Dogun writes on stone              | Dogun en-vrothu ho stod        |
| Korzim wrote a letter to a friend  | Korzim em-vrothu lotod to frod |
| We will speak wynnic and dogun     | ef-spohaa wynnic o dogun       |
| Doguns live                        | Dohearhe en-dohio              |
