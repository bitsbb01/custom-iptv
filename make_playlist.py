import requests

def get_data(url):
    try:
        return requests.get(url).text.split("\n")
    except Exception as e:
        print(e)
        exit(1)


def make_eng():
    url = "https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8"
    data = get_data(url)
    Countries = ("UK", "USA", "Australia", "Ireland", "Canada", "Pluto")
    english_channels = []
    for line in data:
        if "EXTINF" in line and any(country in line for country in Countries):
            channel_link = data[data.index(line) + 1]
            channel = f"{line}\n{channel_link}"
            english_channels.append(channel)
    with open("m3u8/english.m3u8", "w", encoding="utf-8") as eng:
        eng.write("\n".join(english_channels))


def make_esp():
    spanish_channels = []
    url = "https://iptv-org.github.io/iptv/languages/spa.m3u"
    data = get_data(url)
    for line in data:
        if "EXTINF" in line:
            if "group" in line:
                grp_section = line[line.find('group-title="') :]
                group = grp_section.split('"')[1::2][0]
                _line = line.replace(f'group-title="{group}', 'group-title="Spanish')
                if len(group) != 0:
                    _line = f"{_line} [{group}]"
            else:
                _line = line.replace(",", 'group-title="Spanish,')
            channel_link = data[data.index(line) + 1]
            channel = f"{_line}\n{channel_link}"
            spanish_channels.append(channel)

    with open("m3u8/spanish.m3u8", "w", encoding="utf-8") as _spa:
        _spa.write("\n".join(spanish_channels))


def mergefiles(files, outfile):
    with open(outfile, "w") as out:
        for fname in files:
            with open(f"m3u8/{fname}.m3u8") as infile:
                for line in infile:
                    out.write(line)
            out.write('\n')


if __name__ == "__main__":
    filenames = ["kenya", "fashiontv", "english", "spanish"]
    make_eng()
    make_esp()
    mergefiles(filenames, "m3u8/mylist.m3u8")
    filenames.remove("spanish")
    mergefiles(filenames, "m3u8/tv.m3u8")
