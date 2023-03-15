import re
import BYUSpeechDownloader
from mutagen.id3 import ID3, TPE1, TIT2, TDRC, TALB, APIC, ID3NoHeaderError
import urllib.request

YEAR_PARSE_REGEX = "(^\d{4}\s|\s\d{4}\s|\s\d{4}$)"
filename_test = '3244 d2343 lkldh 3245 s;fahdlk 324 hkl;341hjkl; 214 khl21;h2132421 20163 dskfl d3445'


def parse_year(input_str):
    out_str = re.search(YEAR_PARSE_REGEX, input_str)
    if not isinstance(out_str, type(None)):
        out_str = re.sub("\D", "" , out_str.group())
    return out_str

talk_obj = {
    "speaker_url": "http://test.com",
    "speaker": "Elder Holllllland",
    "title": "Lessons From The One and Only, LIBERTY JAIL!",
    "date": "September 7, 2008",
    "year": "2008",
    "mp3_url": "mp3_url",
    "article_tag": "icle",
    "mp3_url_tag": "mp3_url_tag"
}
filename = "Lessons from Liberty Jail - Jeffrey R. Holland - September 7, 2008.mp3"

try:
    audio = ID3(filename)
except ID3NoHeaderError:
    audio = ID3()
audio['TPE1'] = TPE1(encoding=3, text=talk_obj.get('speaker')) # Artist
audio['TIT2'] = TIT2(encoding=3, text=talk_obj.get('title'))   # Title
audio['TDRC'] = TDRC(encoding=3, text=talk_obj.get('year')) # Year
audio['TALB'] = TALB(encoding=3, text=f"BYU Devotionals {talk_obj.get('year')}") # Album

# with open('rap-mixtape-cover-art.jpg', 'rb') as albumart:
albumart_url = "https://speeches.byu.edu/wp-content/uploads/jpg/Bennett_Richard-Web-compressor.jpg"
albumart = urllib.request.urlopen(albumart_url)
audio['APIC'] = APIC(
                    encoding=3,
                    mime='image/jpeg',
                    type=3, desc=u'Cover',
                    data=albumart.read()
                )            
audio.save(filename)


# BYUSpeechDownloader.add_metadata(filename, sample_talk_obj)


# print(f'"{parse_year(filename_test)}"')

# print(re.sub("\D", "" ,re.search(YEAR_PARSE_REGEX, filename_test).group()))
