from __future__ import unicode_literals

import re


# Resolutions
resolution = re.compile(r'(?P<vres>4320|2160|1080|720|480|360)(?P<scan>[pi])', re.IGNORECASE)
widescreen = re.compile(r'\b(w(?:ide)?s(?:creen)?)\b', re.IGNORECASE)

# Sources
tv = re.compile(r'([sph]d).?tv|tv(rip|mux)', re.IGNORECASE)
dvd = re.compile(r'(?P<hd>hd)?dvd(?P<rip>rip|mux)?', re.IGNORECASE)
web = re.compile(r'(web(?P<type>rip|mux|hd|.?dl|\b))', re.IGNORECASE)
bluray = re.compile(r'(blue?-?ray|b[rd](?:rip|mux))', re.IGNORECASE)
sat = re.compile(r'(dsr|satrip)', re.IGNORECASE)
amazon = re.compile(r'(amzn|amazon)(hd|uhd)?', re.IGNORECASE)
itunes = re.compile(r'itunes(hd|uhd)?', re.IGNORECASE)
netflix = re.compile(r'(nf|netflix)(hd|uhd)?', re.IGNORECASE)
aussie = re.compile(r'\b(bf1)\b', re.IGNORECASE)  # aussie p2p release group

# Codecs
avc = re.compile(r'([xh].?26[45]|(?:he|a)vc)', re.IGNORECASE)
xvid = re.compile(r'(xvid|divx)', re.IGNORECASE)
mpeg = re.compile(r'mpeg(-?2)?', re.IGNORECASE)

# anime
anime_sd = re.compile(r'(848x480|480p|360p|xvid)', re.IGNORECASE)
anime_hd = re.compile(r'((1280|960)x720|720p)', re.IGNORECASE)
anime_fullhd = re.compile(r'(1920x1080|1080p)', re.IGNORECASE)
anime_bluray = re.compile(r'(blue?-?ray|b[rd](?:rip|mux)|(?:\b|_)bd(?:\b|_))', re.IGNORECASE)
